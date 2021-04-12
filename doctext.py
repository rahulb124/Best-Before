import argparse
import io
import trial1

from google.cloud import vision
from google.cloud.vision import types



# [START def_detect_text_uri]
def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri
    counter = 0
    response = client.text_detection(image=image)
    texts = response.text_annotations
    result = ""

    for text in texts:
        if(text.description.find("\"")):
            cleaned = text.description.replace("\"","")
            counter += 1
        else:
            cleaned = text.description
        if counter == 2:
            break
        else:
            result += cleaned

    write_file = open("output.txt","w")
    write(result)
    write_file.close()

        #vertices = (['({},{})'.format(vertex.x, vertex.y)
         #           for vertex in text.bounding_poly.vertices])

#        print('bounds: {}'.format(','.join(vertices)))
# [END def_detect_text_uri]


def run_uri(args):
    if args.command == 'text-uri':
        detect_text_uri(args.uri)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')

    text_file_parser = subparsers.add_parser(
        'text-uri', help=detect_text_uri.__doc__)
    text_file_parser.add_argument('uri')

    args = parser.parse_args()

    if ('uri' in args.command):
        run_uri(args)