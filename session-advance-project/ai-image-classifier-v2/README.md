curl -X POST "http://localhost:8000/predict" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/Users/syednadeem/Documents/workspace_project_sessions/project_sessions/session-advance-project/ai-image-classifier/test_data/sameple_dog1.png"
