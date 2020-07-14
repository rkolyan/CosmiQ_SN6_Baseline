import gdal

# Функция: Копирует или перемещает исходноге изображение, изменяя порядок (а также количество) наложения цветовых каналов
# Вход:
# srcpath - строка, путь к исходному изображению
# dstpath - строка, путь к получаемому изображению
# bandlist - список из целых чисел, номера групп растров.
# deletesource - флаг, если установлен - удаление исходного изображения
def reorderbands(srcpath, dstpath, bandlist, deletesource=False):
    """
    Copies a TIFF image from srcpath to dstpath, reordering the bands.
    """
    #Handles special case where source path and destination path are the same
    if srcpath==dstpath:
        #Move file to temporary location before continuing
        srcpath = srcpath + str(uuid.uuid4());
        shutil.move(dstpath, srcpath);
        deletesource = True;

    driver = gdal.GetDriverByName('GTiff');
    tilefile = gdal.Open(srcpath);
    geotransform = tilefile.GetGeoTransform();
    projection = tilefile.GetProjection();
    numbands = len(bandlist);
    shape = tilefile.GetRasterBand(1).ReadAsArray().shape;
    copyfile = driver.Create(dstpath, shape[1], shape[0],
                             numbands, gdal.GDT_Byte);
    for bandnum in range(1, numbands+1):
        banddata = tilefile.GetRasterBand(bandlist[bandnum-1]).ReadAsArray();
        copyfile.GetRasterBand(bandnum).WriteArray(banddata);
    copyfile.SetGeoTransform(geotransform);
    copyfile.SetProjection(projection);
    copyfile.FlushCache();
    copyfile = None;
    tilefile = None;

    if deletesource:
        os.remove(srcpath);

def enter_parameters():
    parameters = dict();
    #TODO: Enter parameters;
    parameters["srcpath"] = input("Введите название изменяемого файла изображения:");
    return parameters;

def create_four_images(srcpath):
    reorderbands(srcpath, "only_red_" + srcpath, [1]);
    reorderbands(srcpath, "only_green_" + srcpath, [2]);
    reorderbands(srcpath, "only_blue_" + srcpath, [3]);
    reorderbands(srcpath, "composite_" + srcpath, [3, 1, 1, 2]);
    #TODO: Create composite [3, 1, 1, 2]

if __name__ == "__main__":
    parameters = enter_parameters();
    create_four_images(parameters["srcpath"]);

    driver = gdal.GetDriverByName("GTiff");
    tilefile = gdal.Open(parameters["srcpath"]);
    #copyfile = driver.CreateCopy("copy_" + parameters["srcpath"], tilefile, strict=0);
    print(tilefile.RasterCount);
    #print(copyfile.RasterCount);
    #reorderbands(parameters["srcpath"], "copy_" + parameters["srcpath"], [3, 1, 1, 2]);
