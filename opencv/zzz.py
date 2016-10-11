{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import argparse\n",
    "import imutils\n",
    "import cv2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "usage: __main__.py [-h] -i IMAGE\n",
      "__main__.py: error: argument -i/--image is required\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "2",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 2\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "To exit: use 'exit', 'quit', or Ctrl-D.\n"
     ]
    }
   ],
   "source": [
    "# construct the argument parse and parse the arguments\n",
    "ap = argparse.ArgumentParser()\n",
    "ap.add_argument(\"-i\", \"--image\", required=True, help=\"path to the input image\")\n",
    "args = vars(ap.parse_args())\n",
    " \n",
    "# load the image, convert it to grayscale, blur it slightly,\n",
    "# and threshold it\n",
    "image = cv2.imread(args[\"image\"])\n",
    "gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n",
    "blurred = cv2.GaussianBlur(gray, (5, 5), 0)\n",
    "thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]\n",
    " \n",
    "# find contours in the thresholded image\n",
    "cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)\n",
    "cnts = cnts[0] if imutils.is_cv2() else cnts[1]\n",
    " \n",
    "# loop over the contours\n",
    "for c in cnts:\n",
    "# compute the center of the contour\n",
    "    M = cv2.moments(c)\n",
    "    cX = int(M[\"m10\"] / M[\"m00\"])\n",
    "    cY = int(M[\"m01\"] / M[\"m00\"])\n",
    " \n",
    "    # draw the contour and center of the shape on the image\n",
    "    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)\n",
    "    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)\n",
    "    cv2.putText(image, \"center\", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)\n",
    "\n",
    "    # show the image\n",
    "    cv2.imshow(\"Image\", image)\n",
    "    cv2.waitKey(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
