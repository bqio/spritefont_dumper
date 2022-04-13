# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Dxtkfont(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = (self._io.read_bytes(8)).decode(u"utf8")
        self.glyphs_count = self._io.read_u4le()
        self.glyphs = [None] * (self.glyphs_count)
        for i in range(self.glyphs_count):
            self.glyphs[i] = Dxtkfont.Glyph(self._io, self, self._root)

        self.line_spacing = self._io.read_f4le()

    class Glyph(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.char = self._io.read_u4le()
            self.left = self._io.read_u4le()
            self.top = self._io.read_u4le()
            self.right = self._io.read_u4le()
            self.bottom = self._io.read_u4le()
            self.x_offset = self._io.read_f4le()
            self.y_offset = self._io.read_f4le()
            self.x_advance = self._io.read_f4le()



