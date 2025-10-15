from flask import Blueprint, jsonify, request, current_app
import cloudinary.uploader

gallery_bp = Blueprint("gallery", __name__)

@gallery_bp.route("/create-memory", methods=["POST"])
def create_memory():
    try:
        # To-Do: Create a way to Identify if the user has enough memo token
        files = request.files.getlist('file')

        if not files or not len(files):
            return jsonify({'msg': 'No file uploaded'}), 400
    

        uploaded_files = []
    
        for file_to_upload in files:

            allowed_types = {'image/png', 'image/jpeg', 'image/jpg', 'video/mp4'}
            if file_to_upload.content_type not in allowed_types:
                continue  

            upload_result = cloudinary.uploader.upload(
                file_to_upload,
                folder="memories",
                resource_type="auto"
            )
            
            # To-Do: Store in Firebase Using User_ID

            uploaded_files.append({
                'cloudinary_url': upload_result['secure_url'],
                'public_id': upload_result['public_id']
            })

        if len(uploaded_files) == 0:
            return jsonify({'msg': 'No valid files uploaded'}), 400

        return jsonify({
            'msg': 'Successfully uploaded memories',
            'files': uploaded_files
        }), 201

    except Exception as e:
        return jsonify({'msg': 'Internal server error', 'error': str(e)}), 500
