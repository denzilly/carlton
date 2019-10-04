import os , array
import pandas as pd
import time


from PIL import Image

# THIS SCRIPT CONVERTS 28x28 PNG IMAGES INTO A CSV FILE OF FORMAT (number of images * 784) so that they can be read into a classifier model
# Remember to add .csv to path
def img_to_csv():

    columnNames = list()


    #Make 784 columns (28x28) prefixed with pixel
    for i in range(784):
        pixel = 'pixel'
        pixel += str(i)
        columnNames.append(pixel)


    train_data = pd.DataFrame(columns = columnNames)
    start_time = time.time()




    #My naming convention is slice_iy, hence double for loop
    # Load image, and append pixel values

    count = 1

    for h in range(0,101):
        for i in range(1,7):
            img_name = 'collected/slice_' + str(h) + str(i) + '.png'
            img = Image.open(img_name)
            rawData = img.load()
            print(img_name)
                #print rawData
            data = []
            for y in range(28):
                for x in range(28):
                    data.append(rawData[x,y][0])

            k = 0
                #print data

            train_data.loc[count] = [data[k] for k in range(784)]
            count += 1


        #print train_data.loc[0]

    zerolist = [0] * (int(count - 1))
    print("done")
    train_data.insert(loc=0, column='label', value=zerolist)

    print ("Done")
    print  (time.time()-start_time)

    #os.chdir('../../')
    #label_data = pd.read_csv("train.csv")
    #print label_data
    #train_labels = label_data['label']
    #print label_data['label']
    #train_data = pd.concat([train_data,label_data],axis = 1)
    #train_data = train_data.drop('filename',1)
    print (train_data)

    #Save file

    train_data.to_csv("testdata_vm.csv",index = False)
    print ("Done1")
    print  (time.time()-start_time)


img_to_csv()
