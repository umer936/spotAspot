initial_img = Image('images/cars3.png')
initial_img.show()
grayed_img = initial_img.colorDistance(Color.GRAY)
grayed_img.show()
img3 = (initial_img - grayed_img) * 3
img3.show()
img4 = img3.findBlobs()
img4.show()
img4[-1].drawHoles(Color.RED)
img4.show()
img5 = img4.image
img5.show()
img6 = img5.morphClose().findBlobs()
img6.show()
img6[-1].drawHoles(Color.RED)
img6.show()
img6.show()