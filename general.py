# coding=utf-8
import tarfile

# http://stackoverflow.com/questions/2032403/how-to-create-full-compressed-tar-file-using-python
# http://stackoverflow.com/questions/3874837/how-do-i-compress-a-folder-with-the-python-gzip-module
name = "PHPZh"
tar = tarfile.open("%s.docset.tgz" % name, "w:gz")
# tar = tarfile.open("TarName.tar.gz", "w:gz")
tar.add(r"D:\OpenSource\doc\%s.docset" % name, arcname=("%s.docset" % name))
tar.close()
# 知道
