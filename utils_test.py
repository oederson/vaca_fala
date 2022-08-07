from utils import formatar_array

def test_deve_trazer_o_array_formatado():
    array_desformatado = ['banana', 'maca', 'uva']
    array_formatado = ['banana', 'maca  ', 'uva   ']
    assert formatar_array(array_desformatado) == array_formatado
