from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

subscription_key = "7c9ff1054a03419eaf3ffed8de65c6c0"
endpoint = "https://azcogsvc.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

'''
Detect Domain-specific Content - remote
This example detects celebrites and landmarks in remote images.
'''
print("===== Detect Domain-specific Content - remote =====")
# URL of one or more celebrities
remote_image_url_celebs = "https://raw.githubusercontent.com/gottagetgit/AI102Files/main/Analyze_images_using_Computer_Vision_API/Images/Faces.jpg"
# Call API with content type (celebrities) and URL
detect_domain_results_celebs_remote = computervision_client.analyze_image_by_domain("celebrities", remote_image_url_celebs)

# Print detection results with name
print("Celebrities in the remote image:")
if len(detect_domain_results_celebs_remote.result["celebrities"]) == 0:
    print("No celebrities detected.")
else:
    for celeb in detect_domain_results_celebs_remote.result["celebrities"]:
        print(celeb["name"])

'''
Detect Domain-specific Content - local
This example detects celebrites and landmarks in local images.
'''
print("===== Detect Domain-specific Content - local =====")
# Open local image file containing a celebritie
local_image_path_celebrity = "../Analyze_images_using_Computer_Vision_API/Images/Faces.jpg"
local_image_celebrity = open(local_image_path_celebrity, "rb")
# Call API with the type of content (celebrities) and local image
detect_domain_results_celebs_local = computervision_client.analyze_image_by_domain_in_stream("celebrities", local_image_celebrity)

# Print which celebrities (if any) were detected
print("Celebrities in the local image:")
if len(detect_domain_results_celebs_local.result["celebrities"]) == 0:
    print("No celebrities detected.")
else:
    for celeb in detect_domain_results_celebs_local.result["celebrities"]:
        print(celeb["name"])