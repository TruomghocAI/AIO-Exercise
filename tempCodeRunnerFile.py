from diffusers import StableDiffusionImg2ImgPipeline
import torch
from PIL import Image

# Khởi tạo pipeline với tham số num_images_per_prompt=5
pipeline = StableDiffusionImg2ImgPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    num_images_per_prompt=5  # Thêm tham số này để giới hạn số lượng files
)
pipeline = pipeline.to("cuda" if torch.cuda.is_available() else "cpu")

# Load ảnh đầu vào
input_image = Image.open("Screenshot 2024-11-03 224847.png").convert("RGB")

# Thiết lập các tham số
strength = 0.6
guidance_scale = 8

# Chạy pipeline với num_inference_steps=5
output_image = pipeline(
    prompt=None, 
    image=input_image, 
    strength=strength, 
    guidance_scale=guidance_scale,
    num_inference_steps=5  # Thêm tham số này để giới hạn số bước inference
).images[0]

# Lưu ảnh đầu ra
output_image.save("/mnt/data/output_image.jpg")
print("Đã lưu ảnh đầu ra tại '/mnt/data/output_image.jpg'")