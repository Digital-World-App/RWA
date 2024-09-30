from django.http import JsonResponse, HttpRequest
from django.shortcuts import render
from dashboard.auto_contract.services.generate_pdf import generate_pdf
from dashboard.auto_contract.services.load_json import load_json
from django.http import HttpRequest
import json
from django.http import HttpResponse
from dashboard.models import (
    LocalizacaoGeografica,
    Prefeitura,
    OficioNotarial,
    Advogado,
    Engenheiro,
    Topografo,
    Imovel,
    PlanoArquitetonico,
    Topografia,
    PlanoDeZoneamento
)


def localizacao_geografica_form(request: HttpRequest):
    if request.method == 'POST':
        # Obtenha os dados do formulário enviado
        pais = request.POST.get('pais')
        estado = request.POST.get('estado')
        municipio = request.POST.get('municipio')
        bairro = request.POST.get('bairro')
        rua = request.POST.get('rua')
        quadra = request.POST.get('quadra')
        lote = request.POST.get('lote')
        cep = request.POST.get('cep')
        numero = request.POST.get('numero')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        categoria = request.POST.get('categoria')

        # Valide os dados recebidos
        errors = {}
        if not pais:
            errors['pais'] = 'O campo país é obrigatório.'
        if not estado:
            errors['estado'] = 'O campo estado é obrigatório.'
        if not municipio:
            errors['municipio'] = 'O campo município é obrigatório.'
        if not bairro:
            errors['bairro'] = 'O campo bairro é obrigatório.'
        if not rua:
            errors['rua'] = 'O campo rua é obrigatório.'
        if not quadra:
            errors['quadra'] = 'O campo quadra é obrigatório.'
        if not lote:
            errors['lote'] = 'O campo lote é obrigatório.'
        if not cep:
            errors['cep'] = 'O campo CEP é obrigatório.'
        if not numero:
            errors['numero'] = 'O campo número é obrigatório.'
        if not latitude:
            errors['latitude'] = 'O campo latitude é obrigatório.'
        if not longitude:
            errors['longitude'] = 'O campo longitude é obrigatório.'
        if not categoria:
            errors['categoria'] = 'O campo categoria é obrigatório.'
        # Adicione mais validações conforme necessário

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        # Crie uma instância do modelo LocalizacaoGeografica com os dados do formulário
        localizacao_geografica = LocalizacaoGeografica(
            pais=pais,
            estado=estado,
            municipio=municipio,
            bairro=bairro,
            rua=rua,
            quadra=quadra,
            lote=lote,
            cep=cep,
            numero=numero,
            latitude=latitude,
            longitude=longitude,
            categoria=categoria
        )

        try:
            localizacao_geografica.save()
        except:
            return JsonResponse({'error': 'Erro ao salvar dados no sistema!'}, status=500)

        # Redirecione o usuário para a página de confirmação ou faça qualquer outra ação necessária
        return JsonResponse({'success': 'Dados Salvos com sucesso!'}, status=201)

    # Se o método da requisição não for POST, renderize a página do formulário
    return render(request, 'pages/blockchain/registration.html')


def prefeitura_form(request: HttpRequest):
    if request.method == 'POST':
        # Obtenha os dados do formulário enviado
        addressCountry = request.POST.get('pais')
        addressStates = request.POST.get('estado')
        municipality = request.POST.get('municipio')
        neighborhood = request.POST.get('bairro')
        street = request.POST.get('rua')
        block = request.POST.get('quadra')
        lot = request.POST.get('lote')
        iptuRegistration = request.POST.get('iptuRegistration')

        # Valide os dados recebidos
        errors = {}
        if not addressCountry:
            errors['addressCountry'] = 'O campo país é obrigatório.'
        if not addressStates:
            errors['addressStates'] = 'O campo estado é obrigatório.'
        if not municipality:
            errors['municipality'] = 'O campo município é obrigatório.'
        if not neighborhood:
            errors['neighborhood'] = 'O campo bairro é obrigatório.'
        if not street:
            errors['street'] = 'O campo rua é obrigatório.'
        if not block:
            errors['block'] = 'O campo quadra é obrigatório.'
        if not lot:
            errors['lot'] = 'O campo lote é obrigatório.'
        if not iptuRegistration:
            errors['iptuRegistration'] = 'O campo número de registro IPTU é obrigatório.'

        # Adicione mais validações conforme necessário

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        # Crie uma instância do modelo Prefeitura com os dados do formulário
        prefeitura = Prefeitura(
            addressCountry=addressCountry,
            addressStates=addressStates,
            municipality=municipality,
            neighborhood=neighborhood,
            street=street,
            block=block,
            lot=lot,
            iptuRegistration=iptuRegistration
        )

        try:
            prefeitura.save()
        except:
            return JsonResponse({'error': 'Erro ao salvar dados da prefeitura no sistema!'}, status=500)

        return JsonResponse({'success': 'Dados salvos da prefeitura salvos com sucesso!'}, status=201)
    # Se o método da requisição não for POST, renderize a página do formulário
    return render(request, 'pages/blockchain/registration.html')


def oficio_notarial_form(request: HttpRequest):
    if request.method == 'POST':
        # Obtenha os dados do formulário enviado
        notarialCountry = request.POST.get('pais')
        notarialStates = request.POST.get('estado')
        notarialMunicipality = request.POST.get('municipio')
        notarialNeighborhood = request.POST.get('bairro')
        notarialStreet = request.POST.get('rua')
        notarialBlock = request.POST.get('quadra')
        notarialLot = request.POST.get('lote')
        notarialRegistration = request.POST.get('notarialRegistration')

        # Valide os dados recebidos
        errors = {}
        if not notarialCountry:
            errors['notarialCountry'] = 'O campo país é obrigatório.'
        if not notarialStates:
            errors['notarialStates'] = 'O campo estado é obrigatório.'
        if not notarialMunicipality:
            errors['notarialMunicipality'] = 'O campo município é obrigatório.'
        if not notarialNeighborhood:
            errors['notarialNeighborhood'] = 'O campo bairro é obrigatório.'
        if not notarialStreet:
            errors['notarialStreet'] = 'O campo rua é obrigatório.'
        if not notarialBlock:
            errors['notarialBlock'] = 'O campo quadra é obrigatório.'
        if not notarialLot:
            errors['notarialLot'] = 'O campo lote é obrigatório.'
        if not notarialRegistration:
            errors['notarialRegistration'] = 'O campo número de registro notarial é obrigatório.'

        # Adicione mais validações conforme necessário

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        # Crie uma instância do modelo OficioNotarial com os dados do formulário
        oficio_notarial = OficioNotarial(
            notarialCountry=notarialCountry,
            notarialStates=notarialStates,
            notarialMunicipality=notarialMunicipality,
            notarialNeighborhood=notarialNeighborhood,
            notarialStreet=notarialStreet,
            notarialBlock=notarialBlock,
            notarialLot=notarialLot,
            notarialRegistration=notarialRegistration
        )

        try:
            oficio_notarial.save()
        except:
            return JsonResponse({'error': 'Erro ao salvar dados do Oficio Notorial no sistema!'}, status=500)

        return JsonResponse({'success': 'Sucesso ao salvar dados do Oficio Notorial no sistema!'}, status=201)

    return render(request, 'pages/blockchain/registration.html')


def topografo_form(request: HttpRequest):
    if request.method == 'POST':
        # Obtenha os dados do formulário enviado
        nome = request.POST.get('nome')
        rg = request.POST.get('rg')
        cpf = request.POST.get('cpf')
        nome_fantasia = request.POST.get('nomeFantasia')
        cnpj = request.POST.get('cnpj')
        registro = request.POST.get('registro')

        # Valide os dados recebidos
        errors = {}
        if not nome:
            errors['nome'] = 'O campo nome é obrigatório.'
        if not rg:
            errors['rg'] = 'O campo RG é obrigatório.'
        if not cpf:
            errors['cpf'] = 'O campo CPF é obrigatório.'
        if not nome_fantasia:
            errors['nome_fantasia'] = 'O campo nome fantasia é obrigatório.'
        if not cnpj:
            errors['cnpj'] = 'O campo CNPJ é obrigatório.'
        if not registro:
            errors['registro'] = f'O campo número de registro do Topógrafo(a) é obrigatório.'

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        # Crie uma instância do modelo Topografo com os dados do formulário
        topografo = Topografo(
            nome=nome,
            rg=rg,
            cpf=cpf,
            nome_fantasia=nome_fantasia,
            cnpj=cnpj,
            registro=registro
        )

        try:
            topografo.save()
        except:
            return JsonResponse({'error': 'Erro ao salvar dados no sistema!'}, status=500)

        return JsonResponse({'success': 'Sucesso ao salvar dados do topógrafo no sistema'}, status=201)

    return render(request, 'pages/blockchain/registration.html')


def engenheiro_form(request: HttpRequest):
    if request.method == 'POST':
        # Obtenha os dados do formulário enviado
        nome = request.POST.get('nome')
        rg = request.POST.get('rg')
        cpf = request.POST.get('cpf')
        nome_fantasia = request.POST.get('nomeFantasia')
        cnpj = request.POST.get('cnpj')
        registro = request.POST.get('registro')

        # Valide os dados recebidos
        errors = {}
        if not nome:
            errors['nome'] = 'O campo nome é obrigatório.'
        if not rg:
            errors['rg'] = 'O campo RG é obrigatório.'
        if not cpf:
            errors['cpf'] = 'O campo CPF é obrigatório.'
        if not nome_fantasia:
            errors['nome_fantasia'] = 'O campo nome fantasia é obrigatório.'
        if not cnpj:
            errors['cnpj'] = 'O campo CNPJ é obrigatório.'
        if not registro:
            errors['registro'] = f'O campo número de registro do Engenheiro(a) é obrigatório.'

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        # Crie uma instância do modelo Engenheiro com os dados do formulário
        engenheiro = Engenheiro(
            nome=nome,
            rg=rg,
            cpf=cpf,
            nome_fantasia=nome_fantasia,
            cnpj=cnpj,
            registro=registro
        )

        try:
            engenheiro.save()
        except:
            return JsonResponse({'error': 'Erro ao tentar salvar os dados do Engenheiro'}, status=500)

        return JsonResponse({'success': 'Sucesso ao salvar dados no sistema!'}, status=201)

    return render(request, 'pages/blockchain/registration.html')


def advogado_form(request: HttpRequest):
    if request.method == 'POST':
        # Obtenha os dados do formulário enviado
        nome = request.POST.get('nome')
        rg = request.POST.get('rg')
        cpf = request.POST.get('cpf')
        nome_fantasia = request.POST.get('nomeFantasia')
        cnpj = request.POST.get('cnpj')
        registro = request.POST.get('registro')

        # Valide os dados recebidos
        errors = {}
        if not nome:
            errors['nome'] = 'O campo nome é obrigatório.'
        if not rg:
            errors['rg'] = 'O campo RG é obrigatório.'
        if not cpf:
            errors['cpf'] = 'O campo CPF é obrigatório.'
        if not nome_fantasia:
            errors['nome_fantasia'] = 'O campo nome fantasia é obrigatório.'
        if not cnpj:
            errors['cnpj'] = 'O campo CNPJ é obrigatório.'
        if not registro:
            errors['registro'] = f'O campo número de registro do Advogado(a) é obrigatório.'

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        # Crie uma instância do modelo Advogado com os dados do formulário
        advogado = Advogado(
            nome=nome,
            rg=rg,
            cpf=cpf,
            nome_fantasia=nome_fantasia,
            cnpj=cnpj,
            registro=registro
        )

        try:
            advogado.save()
        except:
            return JsonResponse({'error': 'Erro ao salvar dados no sistema!'}, status=500)

        return JsonResponse({'success': 'Sucesso ao salvar dados no sistema!'}, status=201)

    return render(request, 'pages/blockchain/registration.html')


def fotos_do_imovel_form(request: HttpRequest):
    if request.method == 'POST':
        # Obtenha os dados do formulário enviado
        preco_venda = request.POST.get('precoVenda')
        currency_venda = request.POST.get('currencyVenda')
        preco_aluguel = request.POST.get('precoAluguel')
        currency_aluguel = request.POST.get('currencyAluguel')
        categoria = request.POST.get('categoria')
        comodos = request.POST.getlist('comodos[]')

        # Valide os dados recebidos
        errors = {}
        if not preco_venda:
            errors['preco_venda'] = 'O campo Preço de Venda é obrigatório.'
        if not preco_aluguel:
            errors['preco_aluguel'] = 'O campo Preço de Aluguel é obrigatório.'
        if not categoria:
            errors['categoria'] = 'O campo Categoria é obrigatório.'
        if not comodos:
            errors['comodos'] = 'Selecione pelo menos um cômodo.'

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        # Crie uma instância do modelo FotosDoImovel com os dados do formulário
        fotos_do_imovel = Imovel(
            preco_venda=preco_venda,
            currency_venda=currency_venda,
            preco_aluguel=preco_aluguel,
            currency_aluguel=currency_aluguel,
            categoria=categoria,
            comodos=comodos
        )

        try:
            fotos_do_imovel.save()
        except:
            return JsonResponse({'error': 'Erro ao salvar dados no sistema!'}, status=500)

        return JsonResponse({'success': 'Sucesso ao salvar dados no sistema'}, status=201)

    return render(request, 'pages/blockchain/registration.html')


def plano_arquitetonico_form(request: HttpRequest):
    if request.method == 'POST':
        # Obtenha os dados do formulário enviado
        metros_quadrados = request.POST.get('metros_quadrados')
        art_numero = request.POST.get('art_numero')

        # Valide os dados recebidos
        errors = {}
        if not metros_quadrados:
            errors['metros_quadrados'] = 'O campo metros quadrados é obrigatório.'
        if not art_numero:
            errors['art_numero'] = 'O campo ART número é obrigatório.'

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        # Crie uma instância do modelo PlanoArquitetonico com os dados do formulário
        plano_arquitetonico = PlanoArquitetonico(
            metros_quadrados=metros_quadrados,
            art_numero=art_numero
        )

        # Salve o objeto no banco de dados
        try:
            plano_arquitetonico.save()
        except:
            return JsonResponse({'error': 'Erro ao salvar o Plano Arquitetônico no sistema!'}, status=500)

        return JsonResponse({'success': 'Plano arquitetônico salvo com sucesso!'}, status=201)

    return render(request, 'pages/blockchain/registration.html')


def topografia_form(request: HttpRequest):
    if request.method == 'POST':
        # Obtenha os dados do formulário enviado
        zona_utm = request.POST.get('zona_utm')
        meridiano_central = request.POST.get('meridiano_central')
        latitude_utm = request.POST.get('latitude_utm')
        longitude_utm = request.POST.get('longitude_utm')
        sistema_geodesico = request.POST.get('sistema_geodesico')

        # Valide os dados recebidos
        errors = {}
        if not zona_utm:
            errors['zona_utm'] = 'O campo Zona UTM é obrigatório.'
        if not meridiano_central:
            errors['meridiano_central'] = 'O campo Meridiano Central é obrigatório.'
        if not latitude_utm:
            errors['latitude_utm'] = 'O campo Latitude UTM é obrigatório.'
        if not longitude_utm:
            errors['longitude_utm'] = 'O campo Longitude UTM é obrigatório.'
        if not sistema_geodesico:
            errors['sistema_geodesico'] = 'O campo Sistema de Referência Geodésico é obrigatório.'

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        # Crie uma instância do modelo Topografia com os dados do formulário
        topografia = Topografia(
            zona_utm=zona_utm,
            meridiano_central=meridiano_central,
            latitude_utm=latitude_utm,
            longitude_utm=longitude_utm,
            sistema_geodesico=sistema_geodesico
        )

        # Salve o objeto no banco de dados
        try:
            topografia.save()
        except:
            return JsonResponse({'error': 'Falha ao tentar salvar os dados no sistema!'}, status=500)

        return JsonResponse({'success': 'Dados salvos com sucesso!'}, status=201)

    return render(request, 'pages/blockchain/registration.html')


def plano_de_zoneamento_form(request: HttpRequest):
    if request.method == 'POST':
        # Obtenha os dados do formulário enviado
        zoning = request.POST.get('zoning')
        # descricao = request.POST.get('descricao')

        # Valide os dados recebidos
        errors = {}
        if not zoning:
            errors['zoning'] = 'O campo Zoneamento é obrigatório.'

        if errors:
            return JsonResponse({'errors': errors}, status=400)
        
        plano_de_zoneamento = PlanoDeZoneamento(
            zoneamento=zoning,
        )

        try:
            plano_de_zoneamento.save()
        except:
            return JsonResponse({'error': 'Erro ao salvar dados no sistema!'}, status=500)

        # Redirecione o usuário para a página de confirmação ou faça qualquer outra ação necessária
        return JsonResponse({'success': 'Sucesso ao salvar dados no sistema!'}, status=201)

    return render(request, 'pages/blockchain/registration.html')

# Pages -> Blockchain -> Registration
def generate_document(request: HttpRequest):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        #Funções para processamento de cada formulário

        #Montagem do JSON
        path_json_template = 'staticfiles/assets/report/template_escritura.json'
        json_escritura = load_json(json_path=path_json_template)

        #Gera Documento
        template_html_url = 'staticfiles/assets/report/report.html'
        css_url = 'staticfiles/assets/report/report.css'

        pdf_content = generate_pdf(
            contract={'documento': json_escritura, 'data': data},
            template_html=template_html_url,
            base_url='staticfiles/assets/report/',
            stylesheets_path=css_url
        )

        response = HttpResponse(pdf_content, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
        return response
        #return render(request, 'pages/blockchain/registration.html')

    return render(request, 'pages/blockchain/registration.html')

