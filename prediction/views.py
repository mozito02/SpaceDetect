from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pickle
import numpy as np
import os
from django.conf import settings
from django.shortcuts import render

# Load the model once when the server starts
model_path = os.path.join(settings.BASE_DIR, 'model', 'SpaceDetect')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

class SpaceDetectView(APIView):
    def get(self, request):
        # If it's a GET request, render a simple HTML form (optional)
        return render(request, 'prediction/form.html')

    def post(self, request):
        try:
            # Extracting data from the request body
            data = request.data
            est_diameter_min = float(data.get('est_diameter_min', None))
            est_diameter_max = float(data.get('est_diameter_max', None))
            relative_velocity = float(data.get('relative_velocity', None))
            miss_distance = float(data.get('miss_distance', None))
            absolute_magnitude = float(data.get('absolute_magnitude', None))

            # Ensure all inputs are provided
            if None in [est_diameter_min, est_diameter_max, relative_velocity, miss_distance, absolute_magnitude]:
                return Response({"error": "All input fields are required."}, status=status.HTTP_400_BAD_REQUEST)

            # Prepare input data for the model
            input_data = np.array([[est_diameter_min, est_diameter_max, 
                                    relative_velocity, miss_distance, 
                                    absolute_magnitude]])

            # Make the prediction (0 = not hazardous, 1 = hazardous)
            prediction = model.predict(input_data)

            # Return the prediction in the response
            return Response({'hazardous': bool(prediction[0])}, status=status.HTTP_200_OK)

        except ValueError:
            return Response({"error": "Invalid input data. Please provide numeric values."}, 
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
