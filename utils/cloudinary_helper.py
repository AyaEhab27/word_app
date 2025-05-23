import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name="duxc6oeju",
    api_key="658624133868188",
    api_secret="DCoO4wlhT3-nMYTr11096S2MmYk"
)

def upload_to_cloudinary(file_url, public_id=None):
    result = cloudinary.uploader.upload(
        file_url,
        resource_type="auto",
        public_id=public_id  
    )
    return result["secure_url"]
