from PIL import Image, ImageDraw
import random
import math

scale = 10
imageWidth = 150 * scale
imageHeight = 150 * scale
image = Image.new("RGB", (imageWidth, imageHeight), "green")
roadwidth = 12


draw = ImageDraw.Draw(image)

def generateVertex(imageWidth, imageHeight, previousVertex, vertexList):
    min_distance = min(imageWidth, imageHeight) / 10  #Jarak minimum antar vertex
    while True:
        edge = random.choice(['x', 'y'])

        if edge == 'x':
            x = previousVertex[0]
            y = random.randint(0, imageHeight)
        else:
            x = random.randint(0, imageWidth)
            y = previousVertex[1]

        #Mencegah overlapping from GPT :v
        # Check distance to all existing vertices
        if all(math.sqrt((x - v[0])**2 + (y - v[1])**2) >= min_distance for v in vertexList):
            # Check distance to all existing segments
            valid_point = True
            for i in range(len(vertexList) - 1):
                x1, y1, _ = vertexList[i]
                x2, y2, _ = vertexList[i + 1]
                distance = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
                if distance < min_distance:
                    valid_point = False
                    break

            if valid_point:
                return x, y, edge

def firstVertex(imageWidth, imageHeight):
    edge = random.choice(['atas', 'bawah', 'kiri', 'kanan'])
    
    if edge == 'atas':
        x = random.randint(0, imageWidth)
        y = 0
    elif edge == 'bawah':
        x = random.randint(0, imageWidth)
        y = imageHeight
    elif edge == 'kiri':
        x = 0
        y = random.randint(0, imageHeight)
    else:
        x = imageWidth
        y = random.randint(0, imageHeight)
        
    return x, y

def lastVertex(imageWidth, imageHeight, previousVertex):
    edge = previousVertex[2]
    if(edge == 'x'):
        edge = 'y'

    if edge == 'x':
        x = previousVertex[0]
        if(previousVertex[1] > imageHeight/2):
            y = imageHeight
        else:
            y = 0
    else:
        if(previousVertex[0] > imageWidth/2):
            x = imageWidth
        else:
            x = 0
        y = previousVertex[1]

    return x, y, edge

num_vertices = 20
vertexList = []

#generate firstVertex
previousVertex = firstVertex(imageWidth, imageHeight)
vertexList.append(previousVertex + ('',))

#generate random Vertex
for _ in range(num_vertices - 2):
    nextVertex = generateVertex(imageWidth, imageHeight, previousVertex, vertexList)
    draw.line((previousVertex[0], previousVertex[1], nextVertex[0], nextVertex[1]), fill='black', width=1*roadwidth)
    #draw.ellipse((nextVertex[0] - 2, nextVertex[1] - 2, nextVertex[0] + 2, nextVertex[1] + 2), fill='red')
    previousVertex = nextVertex
    vertexList.append(nextVertex)

#generate lastVertex
endVertex = lastVertex(imageWidth, imageHeight, previousVertex)
vertexList.append(endVertex)
draw.line((previousVertex[0], previousVertex[1], endVertex[0], endVertex[1]), fill='black', width=1*roadwidth)

print(vertexList)
image.show()