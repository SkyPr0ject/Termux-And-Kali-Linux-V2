import zlib,base64
exec(zlib.decompress(base64.b64decode("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")))