from osl154ua import signdata

def test_list_signs(capfd):
    assert signdata.list_signs() is None
    out = capfd.readouterr().out
    assert len(out) > 0
