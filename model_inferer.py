import os
import torch
from torch.utils.data import DataLoader
from monai.data import Dataset
from monai.inferers import sliding_window_inference
from monai.networks.nets import SwinUNETR
from monai.transforms import (
    Activations,
    AsDiscrete,
    Compose,
    SaveImage,
    Orientation,
    Spacing,
    ScaleIntensityRange,
    SpatialPad,
    EnsureType,
    LoadImage,
    Invert,
)

model_path = "./models/model.pt"


# output path is always of form f"{output_dir}/{volume_path - ".nii.gz"}_trans.nii.gz"
def infer_with_model(volume_path, output_dir):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    preprocessing = Compose(
        [
            LoadImage(ensure_channel_first=True, image_only=True),
            Orientation(axcodes="RAS"),
            Spacing(
                pixdim=[1.5, 1.5, 2.0],
                mode="bilinear",
            ),
            ScaleIntensityRange(
                a_min=-175,
                a_max=250,
                b_min=0.0,
                b_max=1.0,
                clip=True,
            ),
            SpatialPad(spatial_size=[96, 96, 96]),
            EnsureType(),
        ]
    )

    postprocessing = Compose(
        [
            Activations(softmax=True),
            Invert(
                transform=preprocessing,
                nearest_interp=False,
                to_tensor=True,
            ),
            AsDiscrete(argmax=True),
            SaveImage(
                output_dir=output_dir,
                resample=False,
                squeeze_end_dims=True,
                separate_folder=False,
            ),
        ]
    )

    dataset = Dataset(
        data=[volume_path],
        transform=preprocessing,
    )
    dataloader = DataLoader(dataset=dataset, batch_size=1, num_workers=1)

    network_def = SwinUNETR(
        spatial_dims=3,
        img_size=96,
        in_channels=1,
        out_channels=7,
        feature_size=48,
        use_checkpoint=True,
    )
    model = network_def.to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))

    model.eval()
    with torch.no_grad():
        # this loop always has one iteration
        for data in dataloader:
            image = data.to(device)
            outputs = sliding_window_inference(
                inputs=image,
                roi_size=(96, 96, 96),
                sw_batch_size=1,
                predictor=model,
                overlap=0.25,
            )
            result = postprocessing(outputs[0])

    volume_path_stem = os.path.basename(volume_path)[:-7]
    return result, f"{output_dir}/{volume_path_stem}_trans.nii.gz"
