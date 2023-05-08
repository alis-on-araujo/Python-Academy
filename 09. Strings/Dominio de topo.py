def usuarios_por_pais(emails, tlds):

    dic = {}

    for email in emails:

        idx = email.find('@')
        usuario = email[:idx]
        topo = email[-2:]

        pais = tlds[topo]

        if pais not in dic:

            dic[pais] = [usuario]

        else:

            dic[pais].append(usuario)

    return dic