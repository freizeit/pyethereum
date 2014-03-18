# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# pyethereum is free software: you can redistribute it and/or modify it
# under the terms of the The MIT License


"""Tests related to the trie.Trie class."""


import rlp
import utils


class TestRLP:
    def test_encoding(self):
        tdata = utils.load_test_data("rlptest.json")
        for tn, td in tdata.iteritems():
            sample = td["in"]
            expected = td["out"]
            actual = rlp.encode(sample).encode('hex')
            assert expected == actual, (
                "RLPEncode mismatch for sample '%s'; expected='%s' - "
                "actual='%s'" % (sample, expected, actual))

    def test_decoding(self):
        tdata = utils.load_test_data("rlptest.json")
        for tn, td in tdata.iteritems():
            expected = td["in"]
            sample = td["out"]
            actual = rlp.decode(sample.decode('hex'))
            assert expected == actual, (
                "RLPDecode mismatch for sample '%s'; expected='%s' - "
                "actual='%s'" % (sample, expected, actual))
