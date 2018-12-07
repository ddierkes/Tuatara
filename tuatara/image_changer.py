from PIL import Image, ImageOps


def dimensional_corrector(ratio, sizetup):
        """
        adjust the height and width of an image to match an aspect ratio
        returned height and width must be less than or equal to the inputs
        """
        newRatio = float(sizetup[0])/float(sizetup[1])
        if newRatio < ratio:
            newtup = (sizetup[0], int(float(sizetup[0])/ratio))
        elif newRatio > ratio:
            newtup = (int(float(sizetup[1])*ratio), sizetup[1])
        else:
            newtup = sizetup
        return newtup


def main(filepath, region, size, rotation, quality, format):
    img = Image.open(filepath)
    width, height = img.size
    print(width)
    print(filepath)

    # Region =============================================
    if region == "full":
        pass
    elif region == "square":
        if width > height:
            img = ImageOps.fit(img, (height, height))
        elif height > width:
            img = ImageOps.fit(img, (width, width))
        else:
            pass
    elif region.startswith("pct:"):
        try:
            a, b, c, d = region[4:].split(',')
            left = int((float(a)/100)*width)
            top = int((float(b)/100)*height)
            right = int(left + (float(c)/100)*width)
            bottom = int(top + (float(d)/100)*height)
            boxtup = (left, top, right, bottom)
            img = img.crop(boxtup)
        except Exception:
            return False, ("The percent values entered as a region are "
                           "incorrectly formatted")

    else:
        try:
            x = region.split(',')
            a, b, c, d = x
            left = int(float(a))
            top = int(float(b))
            right = int(left + float(c))
            bottom = int(top + float(d))
            boxtup = (left, top, right, bottom)
            img = img.crop(boxtup)
        except Exception:
            return False, "The region input is incorrectly formatted"

    # Size ==============================================
    width, height = img.size
    ratio = float(width)/float(height)
    if size.startswith("!"):
        size = size[1:]
        sizeCorrect = True
    else:
        sizeCorrect = False

    if size == "full":
        pass
    elif size == "max":
        pass
    elif size.startswith("!"):
        print('starts with !')

    elif size.startswith("pct:"):
        sizeValues = size[4:].split(',')
        if int(sizeValues[0]) < 101 and int(sizeValues[1]) < 101:
            sizetup = (
                int(width*(float(sizeValues[0])/100)),
                int(height*(float(sizeValues[1])/100))
            )
            img = img.resize(sizetup)
        else:
            return False, "Size percentages are too big"
    else:
        sizeValues = size.split(',')
        if sizeValues[0] == "":
            scalePercent = float(sizeValues[1])/height
            newWidth = int(width*scalePercent)
            sizetup = (newWidth, int(sizeValues[1]))
        elif sizeValues[1] == "":
            scalePercent = float(sizeValues[0])/width
            newHeight = int(height*scalePercent)
            sizetup = (int(sizeValues[0]), newHeight)
        else:
            sizetup = (int(sizeValues[0]), int(sizeValues[1]))
        if sizeCorrect:
            sizetup = dimensional_corrector(ratio, sizetup)
        img = img.resize(sizetup)

    # Rotation =============================================
    if rotation.startswith('!'):
        img = ImageOps.mirror(img)
        rotation = rotation[1:]
    try:
        rotation = -float(rotation)
    except Exception:
        # probably input a string
        return False, "The rotation value should be a number"
    img = img.rotate(int(rotation))

    # Quality =============================================
    if quality == 'gray':
        img = ImageOps.grayscale(img)
    elif quality == 'bitonal':
        img = img.convert('1')
    elif quality == 'color':
        img = img.convert('RGB')
    elif quality == 'default':
        pass
    else:
        # return bad 400
        return False, (f"the request for a {quality} quality image is "
                       "unavailable")

    # Format ================================================
    print(filepath)
    print(format)
    filepathparts = filepath.split('.')
    newfilepath = filepathparts[0] + '.' + format
    if format == 'jpg':
        img = img.convert('RGB')
        img.save(newfilepath, "JPEG")
    elif format == 'png':
        img.save(newfilepath, "PNG")
    elif format == 'tif':
        img.save(newfilepath, "TIFF")
    elif format == 'gif':
        img.save(newfilepath, "GIF")
    elif format == 'jp2':
        img.save(newfilepath, "JPEG2000")
    elif format == 'webp':
        img.save(newfilepath, "WEBP")
    elif format == 'pdf':
        img.save(newfilepath, "PDF", resolution=100.0)
    else:
        return False, "An unacceptable file format has been requested"

    return True, newfilepath
