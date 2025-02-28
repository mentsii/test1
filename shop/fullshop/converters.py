class TwoConverorNumbers:
    regex = "[0-9]{2}"

    def to_python(self, значение):
        return int(значение)

    def to_url(self, значение):
        return "%02d" % значение