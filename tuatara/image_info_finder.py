import collections

from PIL import Image


baseInfo = collections.OrderedDict()
baseInfo["@context"] = "http://iiif.io/api/image/2/context.json"
baseInfo["@id"] = ""
baseInfo["@type"] = "iiif:Image"
baseInfo["protocol"] = "http://iiif.io/api/image"
baseInfo["width"] = ""
baseInfo["height"] = ""
baseInfo["profile"] = [
    "http://iiif.io/api/image/2/level2.json", collections.OrderedDict()
]
baseInfo["profile"][1]["supports"] = [
    "baseUriRedirect",
    "cors",
    "mirroring",
    "regionByPct",
    "regionByPx",
    "regionSquare",
    "rotationBy90s",
    "rotationArbitrary",
    "sizeAboveFull",
    "sizeByConfinedWh",
    "sizeByDistoredWh",
    "sizebyH",
    "sizeByPct",
    "sizeByW",
    "sizeByWh",

    "regionSquare",
]
baseInfo["profile"][1]["qualities"] = ["default", "color", "gray", "bitonal"]
baseInfo["profile"][1]["formats"] = ["jpg", "tif", "pdf", "png", "gif", "webp"]


def main(filename, filepath):
    img = Image.open(filepath)
    width, height = img.size
    newInfo = baseInfo.copy()
    newInfo["@id"] = "https://images.mohistory.org/" + filename
    newInfo["height"] = height
    newInfo["width"] = width
    return newInfo
