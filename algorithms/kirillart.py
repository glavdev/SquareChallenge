
def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    return edged

def square(image):
    # вырежем центральную часть
    image = image[100:1700, 350:2050]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    wide = cv2.Canny(blurred, 10, 200)
    tight = cv2.Canny(blurred, 225, 250)
    auto = auto_canny(blurred)

    #find contours
    contours, _ = cv2.findContours(auto, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # new openCV

    pl=0
    for cnt in contours:
      rect = cv2.minAreaRect(cnt)
      box = cv2.cv.BoxPoints(rect)
      box = np.int0(box)
      #find bigges box
      if pl < abs((box[1][0]-box[3][0])*(box[1][1]-box[3][1])):
         box1 = box
         pl = abs((box[1][0]-box[3][0])*(box[1][1]-box[3][1]))

    cv2.drawContours(image,[box1],0,(255,0,0),2)

    # calc sides
    d1 = math.hypot(box1[0][0]-box1[1][0],box1[0][1]-box1[1][1])
    d2 = math.hypot(box1[1][0]-box1[2][0],box1[1][1]-box1[2][1])
    d3 = math.hypot(box1[2][0]-box1[3][0],box1[2][1]-box1[3][1])
    d4 = math.hypot(box1[3][0]-box1[0][0],box1[3][1]-box1[0][1])

    #add coefficient
    pl = ((d1+d3)/2)*((d2+d4)/2)

    return pl
