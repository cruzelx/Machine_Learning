from google_images_download import google_images_download
import sys
response=google_images_download.googleimagesdownload()
for keywords in range(len(sys.argv)):
    print (keywords)
    if(sys.argv[keywords]==sys.argv[0]): continue 
    arguments={"keywords":"{}".format(sys.argv[keywords]),"limit":"500","output_directory":"/home/iamlex/Desktop/Neural_Network/datasets","chromedriver":"/home/iamlex/chromedrive/chromedriver"}
    absimgpath=response.download(arguments)
