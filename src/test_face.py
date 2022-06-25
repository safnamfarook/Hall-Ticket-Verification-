import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
from PIL import Image
import cognitive_face as CF
from io import BytesIO
class test_face:
    def test_face(self,img):
        # Replace <Subscription Key> with your valid subscription key.
        subscription_key = "ce745bddfaf747edaa0ffdfbd5a9f7b6"
        assert subscription_key

        # You must use the same region in your REST call as you used to get your
        # subscription keys. For example, if you got your subscription keys from
        # westus, replace "westcentralus" in the URI below with "westus".
        #
        # Free trial subscription keys are generated in the westcentralus region.
        # If you use a free trial subscription key, you shouldn't need to change
        # this region.
        face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

        # Set image_url to the URL of an image that you want to analyze.


        headers = {'Ocp-Apim-Subscription-Key': subscription_key}
        params = {
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'true',
            'returnFaceAttributes': 'age,gender'
        }
        image_path = img
        print("img--------"+image_path)
        # image_path = "static/photos/1.jpg"
        image_data = open(image_path, "rb").read()
        # data = {'url': image_url}
        # print(data)
        # response = requests.post(face_api_url, params=params, headers=headers, json=data)
        # faces = response.json()

        headers = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "application/octet-stream"}
        response = requests.post(face_api_url, headers=headers,params=params, data=image_data)
        response.raise_for_status()
        faces = response.json()
        # analysis

        print("faces is"+str(faces))
        # Display the original image and overlay it with the face information.
        image = Image.open(image_path)
        # plt.figure(figsize=(8,8))
        # import numpy as np

        # im = np.array(image, dtype=np.uint8)
        #
        # ax = plt.imshow(im, alpha=0.6)
        # print(faces)
        for face in faces:
            fr = face["faceRectangle"]
            fa = face["faceAttributes"]
            fl = face["faceLandmarks"]
            origin = (fr["left"], fr["top"])
            # p = patches.Rectangle(
            #     origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')
            # # ax.axes.add_patch(p)
            # # plt.text(origin[0], origin[1], "%s, %d"%(fa["gender"].capitalize(), fa["age"]),
            #          fontsize=20, weight="bold", va="bottom")
        # _ = plt.axis("off")
        # plt.show()
        # print("fr is"+str(fr))
        # print("fl is"+str(fl))
        # example_dict.get('key1', {}).get('key2')
        plx=fl.get("pupilLeft", {}).get('x')
        ply = fl.get("pupilLeft", {}).get('y')
        prx = fl.get("pupilRight", {}).get('x')
        pry = fl.get("pupilRight", {}).get('y')
        frw=fr.get("width","none")
        import math
        age = math.sqrt(((plx - prx) * (plx - prx)) + ((pry - ply) * (pry - ply)))
        ipd = age / frw
        print(ipd)
        x1 = fl.get("eyeLeftOuter", {}).get('x')
        x2 = fl.get("eyeLeftOuter", {}).get('y')
        x3 = fl.get("eyeRightOuter", {}).get('x')
        x4 = fl.get("eyeRightOuter", {}).get('y')
        x5 = fl.get("eyeLeftInner", {}).get('x')
        x6 = fl.get("eyeLeftInner", {}).get('y')
        x7 = fl.get("eyeRightInner", {}).get('x')
        x8 = fl.get("eyeRightInner", {}).get('y')
        icd = math.sqrt(((x5 - x7) * (x5 - x7)) + ((x6 - x8) * (x6 - x8))) / frw;
        print(icd)
        ocd = math.sqrt(((x1 - x3) * (x1 - x3)) + ((x2 - x4) * (x2 - x4))) / frw;
        print(ocd)
        # rt=str(ipd)+"#"+str(icd)+"#"+str(ocd)
        # print(rt)
        return str(ipd)+"#"+str(icd)+"#"+str(ocd)
    def test_face1(self,img,img1):
        # Replace <Subscription Key> with your valid subscription key.
        subscription_key = "ce745bddfaf747edaa0ffdfbd5a9f7b6"
        assert subscription_key

        # You must use the same region in your REST call as you used to get your
        # subscription keys. For example, if you got your subscription keys from
        # westus, replace "westcentralus" in the URI below with "westus".
        #
        # Free trial subscription keys are generated in the westcentralus region.
        # If you use a free trial subscription key, you shouldn't need to change
        # this region.
        face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

        # Set image_url to the URL of an image that you want to analyze.


        headers = {'Ocp-Apim-Subscription-Key': subscription_key}
        params = {
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'true',
            'returnFaceAttributes': 'age,gender'
        }
        image_path = img
        print("img--------"+image_path)
        # image_path = "static/photos/1.jpg"
        image_data = open(image_path, "rb").read()
        # data = {'url': image_url}
        # print(data)
        # response = requests.post(face_api_url, params=params, headers=headers, json=data)
        # faces = response.json()

        headers = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "application/octet-stream"}
        response = requests.post(face_api_url, headers=headers,params=params, data=image_data)
        response.raise_for_status()
        faces = response.json()
        # analysis

        print("faces is"+str(faces))
        # Display the original image and overlay it with the face information.
        image = Image.open(image_path)
        # plt.figure(figsize=(8,8))
        # import numpy as np

        # im = np.array(image, dtype=np.uint8)
        #
        # ax = plt.imshow(im, alpha=0.6)
        # print(faces)
        fr=[]
        fl=[]
        if faces is not None and len(faces)>0:
            for face in faces:
                fr = face["faceRectangle"]
                fa = face["faceAttributes"]
                fl = face["faceLandmarks"]
            origin = (fr["left"], fr["top"])
            # p = patches.Rectangle(
            #     origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')
            # ax.axes.add_patch(p)
            # plt.text(origin[0], origin[1], "%s, %d"%(fa["gender"].capitalize(), fa["age"]),
            #          fontsize=20, weight="bold", va="bottom")
        # _ = plt.axis("off")
        # plt.show()
        # print("fr is"+str(fr))
        # print("fl is"+str(fl))
        # example_dict.get('key1', {}).get('key2')
            plx=fl.get("pupilLeft", {}).get('x')
            ply = fl.get("pupilLeft", {}).get('y')
            prx = fl.get("pupilRight", {}).get('x')
            pry = fl.get("pupilRight", {}).get('y')
            frw=fr.get("width","none")
            import math
            age = math.sqrt(((plx - prx) * (plx - prx)) + ((pry - ply) * (pry - ply)))
            ipd = age / frw
            print(ipd)
            x1 = fl.get("eyeLeftOuter", {}).get('x')
            x2 = fl.get("eyeLeftOuter", {}).get('y')
            x3 = fl.get("eyeRightOuter", {}).get('x')
            x4 = fl.get("eyeRightOuter", {}).get('y')
            x5 = fl.get("eyeLeftInner", {}).get('x')
            x6 = fl.get("eyeLeftInner", {}).get('y')
            x7 = fl.get("eyeRightInner", {}).get('x')
            x8 = fl.get("eyeRightInner", {}).get('y')
            icd = math.sqrt(((x5 - x7) * (x5 - x7)) + ((x6 - x8) * (x6 - x8))) / frw;
            print(icd)
            ocd = math.sqrt(((x1 - x3) * (x1 - x3)) + ((x2 - x4) * (x2 - x4))) / frw;
            print(ocd)
            # rt=str(ipd)+"#"+str(icd)+"#"+str(ocd)
            # print(rt)
            siml="na"
            try:

                key = 'ce745bddfaf747edaa0ffdfbd5a9f7b6'  # Replace with a valid Subscription Key here.
                CF.Key.set(key)
                base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
                CF.BaseUrl.set(base_url)
                # fc = img
                # fc = CF.face.detect(fc)
                faces1 = CF.face.detect('static/students/'+img1)

                # print(faces, fc)
                # for fc1 in fc:

                similarity = CF.face.verify(faces1[0]['faceId'], faces[0]['faceId'])
                if similarity['isIdentical']:
                    siml="ok"
            except Exception as e:
                print(e)
                sssss=e
                pass


            return str(ipd)+"#"+str(icd)+"#"+str(ocd)+"#"+siml
        else:
            return "0#0#0#na"

