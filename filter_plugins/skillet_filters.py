#!/usr/bin/env python3

# Copyright (c) 2019, Palo Alto Networks
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from passlib.hash import md5_crypt
from passlib.hash import des_crypt
from passlib.hash import sha512_crypt
from base64 import urlsafe_b64decode, urlsafe_b64encode


class FilterModule(object):
    def filters(self):
        return {
            'md5_hash': self.md5_hash,
            'des_hash': self.des_hash,
            'sha512_hash': self.sha512_hash,
            'b64encode': self.b64encode,
            'b64decode': self.b64decode
        }

    def md5_hash(self, txt):
        return md5_crypt.hash(txt)


    def des_hash(self, txt):
        return des_crypt.hash(txt)


    def sha512_hash(self, txt):
        return sha512_crypt.hash(txt)


    def b64encode(self, txt):
        return urlsafe_b64encode(txt)


    def b64decode(self, txt):
        return urlsafe_b64decode(txt)