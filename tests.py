from nose.tools import assert_raises
from nose.tools import eq_

from kata import List


class TestSimpleList():

    def test_find(self):
        list_ = List()
        with assert_raises(KeyError):
            list_.find("fred")

    def test_add(self):
        list_ = List()
        list_.add("fred")
        eq_("fred", list_.find("fred").get_value())
        with assert_raises(KeyError):
            list_.find("wilma")

        list_.add("wilma")
        eq_("fred",  list_.find("fred").get_value())
        eq_("wilma", list_.find("wilma").get_value())
        eq_(["fred", "wilma"], list_.get_values())

    def test_delete(self):
        list_ = List()
        list_.add("fred")
        list_.add("wilma")
        list_.add("betty")
        list_.add("barney")
        eq_(["fred", "wilma", "betty", "barney"], list_.get_values())
        list_.delete("wilma")
        eq_(["fred", "betty", "barney"], list_.get_values())
        list_.delete("barney")
        eq_(["fred", "betty"], list_.get_values())
        list_.delete("fred")
        eq_(["betty"], list_.get_values())
        list_.delete("betty")
        eq_([], list_.get_values())
