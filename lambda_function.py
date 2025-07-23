import json
from urllib.parse import parse_qs
import datetime
import pg8000.native
from typing import Optional, List
from datetime import datetime
from dataclasses import dataclass, field, asdict, fields



# Conexion con la base de datos
def connection():
    return pg8000.native.Connection(
        host="db-aws-instace.cr6acsua6egs.us-east-2.rds.amazonaws.com",
        port=5432,
        database="aws_database",
        user="postgres",
        password="Selva.2025",
        )



# funcion para crear la tabla de la base de datos si no existe
def createDB():
    conn = connection()
    try:
        conn.run("""
        CREATE TABLE IF NOT EXISTS usuariospruebajuan (
            id SERIAL PRIMARY KEY,
            status TEXT,
            lastedited TIMESTAMP WITH TIME ZONE,
            created_at TIMESTAMPTZ DEFAULT now(),
            campaigncount INTEGER,

            name TEXT,         
            type TEXT,
            age INTEGER,
            locations TEXT[],
            education TEXT,
            job TEXT,
            income TEXT,
            businessunit TEXT,
            brandrelationship TEXT,
            digitalchannels TEXT[],
            otherchannelslist TEXT[],
            decisionmaking TEXT,

            currentactivity TEXT,
            satisfactionlevel TEXT,
            autonomylevel TEXT,
            teamsize TEXT,
            dreamsvision TEXT,
            successfeeling TEXT,

            superficialpains TEXT[],
            rootpains TEXT[],
            emotionalload TEXT,
            dailymanifestation TEXT,
            transformationcost TEXT,
            emotionalwound TEXT,
            previoussolutions TEXT,
            searchhistory TEXT,

            triggers TEXT[],
            objectives TEXT[],
            consciousnesslevel TEXT,

            archetype TEXT,
            narrativestyle TEXT,
            connectionstimulus TEXT,
            emotionalpurchasebehavior TEXT,

            narrativestory TEXT,

            pain TEXT[],
            solution TEXT[],
            before TEXT[],
            after TEXT[],
            visualreflection TEXT,
            impactedbycampaign BOOLEAN,
            campaignlinks TEXT
        );
    """)
    finally:
        conn.close()


# Funcion que sirve para inicializar los valores
def preparar_body_para_sql(raw_body: dict) -> dict:
    body = raw_body.copy()
    # Correcciones de nombres
    body["locations"] = raw_body.get("locations", [])
    body["otherchannelslist"] = [raw_body.get("otherchannelslist", "")]

    # Defaults para campos esperados
    defaults = {
        "status": None,
        "lastedited": datetime.utcnow(),
        "created_at": datetime.utcnow(),
        "campaigncount": None,
        "name": None,
        "type": None,
        "age": None,
        "locations": None,
        "education": None,
        "job": None,
        "income": None,
        "businessunit": None,
        "brandrelationship": None,
        "digitalchannels": None,
        "otherchannelslist": None,
        "decisionmaking": None,
        "currentactivity": None,
        "satisfactionlevel": None,
        "autonomylevel": None,
        "teamsize": None,
        "dreamsvision": None,
        "successfeeling": None,
        "superficialpains": None,
        "rootpains": None,
        "emotionalload": None,
        "dailymanifestation": None,
        "transformationcost": None,
        "emotionalwound": None,
        "previoussolutions": None,
        "searchhistory": None,
        "triggers": None,
        "objectives": None,
        "consciousnesslevel": None,
        "archetype": None,
        "narrativestyle": None,
        "connectionstimulus": None,
        "emotionalpurchasebehavior": None,
        "narrativestory": None,
        "pain": None,
        "solution":  None,
        "before": None,
        "after": None,
        "visualreflection": None,
        "impactedbycampaign": False,
        "campaignlinks": None
    }

    for key, value in defaults.items():
        body.setdefault(key, value)

    return body




# Crear clase para obtener columnas a buscaar
@dataclass
class UsuarioIn():
    id: Optional[int] = None
    status: Optional[str] = None
    lastEdited: Optional[datetime] = None
    created_at: Optional[datetime] = None
    campaignCount: Optional[int] = None

    #1
    name: Optional[str] = None
    type: Optional[str] = None
    age: Optional[int] = None
    locations: Optional[List[str]] = None
    education: Optional[str] = None
    job: Optional[str] = None
    income: Optional[str] = None
    businessUnit: Optional[str] = None#en el 1
    brandRelationship: Optional[str] = None
    digitalChannels: Optional[List[str]] = None
    otherChannelsList: Optional[List[str]] = None
    decisionMaking: Optional[str] = None

    # SituationDreamsTab
    currentActivity: Optional[str] = None
    satisfactionLevel: Optional[str] = None
    autonomyLevel: Optional[str] = None
    teamSize: Optional[str] = None
    dreamsVision: Optional[str] = None
    successFeeling: Optional[str] = None

    # PainBlockageTab
    #painMappings: Optional[List[PainMapping]] = None
    superficialPains:Optional[List[str]] = None
    rootPains: Optional[List[str]] = None
    emotionalLoad: Optional[str] = None
    dailyManifestation: Optional[str] = None
    transformationCost: Optional[str] = None
    emotionalWound: Optional[str] = None
    previousSolutions: Optional[str] = None
    searchHistory: Optional[str] = None

    # MotivationConsciousnessTab
    triggers: Optional[List[str]] = None
    objectives: Optional[List[str]] = None
    consciousnessLevel: Optional[str] = None

    # ArchetypeNarrativeTab
    archetype: Optional[str] = None
    narrativeStyle: Optional[str] = None
    connectionStimulus: Optional[str] = None
    emotionalPurchaseBehavior: Optional[str] = None

    # NarrativeProfileTab
    narrativeStory: Optional[str] = None

    # TransformationMapTab
    #transformationTable: Optional[List[TransformationItem]] = None
    pain: Optional[List[str]] = None
    solution: Optional[List[str]] = None
    before: Optional[List[str]] = None
    after: Optional[List[str]] = None
    visualReflection: Optional[str] = None
    impactedByCampaign: Optional[bool] = None
    campaignLinks: Optional[str] = None

class UsuarioOut(UsuarioIn):
    id: int




# Funcion para listar la informacion de la base de datos
def listar_usuarios():
    createDB()
    conn = connection()
    try:
        filas = conn.run("""
        SELECT
        id,
        status,
        lastedited AS "lastEdited",
        created_at,
        campaigncount AS "campaignCount",
        name,
        type,
        age,
        locations,
        education,
        job,
        income,
        businessunit AS "businessUnit",
        brandrelationship AS "brandRelationship",
        digitalchannels AS "digitalChannels",
        otherchannelslist AS "otherChannelsList",
        decisionmaking AS "decisionMaking",
        currentactivity AS "currentActivity",
        satisfactionlevel AS "satisfactionLevel",
        autonomylevel AS "autonomyLevel",
        teamsize AS "teamSize",
        dreamsvision AS "dreamsVision",
        successfeeling AS "successFeeling",
        superficialpains as "superficialPains",
        rootpains as "rootPains",
        emotionalload AS "emotionalLoad",
        dailymanifestation AS "dailyManifestation",
        transformationcost AS "transformationCost",
        emotionalwound AS "emotionalWound",
        previoussolutions AS "previousSolutions",
        searchhistory AS "searchHistory",
        triggers,
        objectives,
        consciousnesslevel AS "consciousnessLevel",
        archetype,
        narrativestyle AS "narrativeStyle",
        connectionstimulus AS "connectionStimulus",
        emotionalpurchasebehavior AS "emotionalPurchaseBehavior",
        narrativestory AS "narrativeStory",
        pain,
        solution,
        before,
        after,
        visualreflection AS "visualReflection",
        impactedbycampaign AS "impactedByCampaign",
        campaignlinks AS "campaignLinks"
        FROM usuariospruebajuan
        """)

        resultados = []
        
        columnas = [f.name for f in fields(UsuarioOut)]
        for fila in filas:
            fila_dict = dict(zip(columnas, fila))
            resultados.append(UsuarioOut(**fila_dict))

        print("Columnas:", columnas)
        print("Fila:", fila)
        print("Fila zip:", dict(zip(columnas, fila)))


        return resultados

    finally:
        conn.close()


# Funcion para insertar informacion en la base de datos
def insertaEnDB(body):

    conn = connection()
    if conn:
        print("Conexión exitosa")
    else:
        print("No se pudo conectar")
    
    body = preparar_body_para_sql(body)
    print("Claves recibidas:", list(body.keys()))
    #body["businessunit"] = body.pop("businessUnit", "")

    try:
        conn.run("""
            INSERT INTO usuariospruebajuan (
                name, status, archetype, businessunit, lastedited, campaigncount, type, age,
                locations, education, job, income, brandrelationship, digitalchannels, otherchannelslist,
                decisionmaking, currentactivity, satisfactionlevel, autonomylevel, teamsize, dreamsvision,
                successfeeling, superficialpains, emotionalload, dailymanifestation, transformationcost,
                emotionalwound, previoussolutions, searchhistory, triggers, objectives, consciousnesslevel,
                narrativestyle, connectionstimulus, emotionalpurchasebehavior,
                narrativestory, after, visualreflection, impactedbycampaign, campaignlinks
            )
            VALUES (
                :name, :status, :archetype, :businessunit, :lastedited, :campaigncount, :type, :age,
                :locations, :education, :job, :income, :brandrelationship, :digitalchannels, :otherchannelslist,
                :decisionmaking, :currentactivity, :satisfactionlevel, :autonomylevel, :teamsize, :dreamsvision,
                :successfeeling, :superficialpains, :emotionalload, :dailymanifestation, :transformationcost,
                :emotionalwound, :previoussolutions, :searchhistory, :triggers, :objectives, :consciousnesslevel,
                :narrativestyle, :connectionstimulus, :emotionalpurchasebehavior,
                :narrativestory, :after, :visualreflection, :impactedbycampaign, :campaignlinks
            )
            """,
        **body
        )
    finally:
        conn.close()



def editarEnDB(id_usuario, body):

    id_usuario = body.pop("id")               # lo sacamos y eliminamos de body
    conn = connection()
    if conn:
        print("Conexión exitosa")
    else:
        print("No se pudo conectar")
    
    body = preparar_body_para_sql(body)
    print("Claves recibidas:", list(body.keys()))
    #body["businessunit"] = body.pop("businessUnit", "")

    try:
        conn.run("""
            UPDATE usuariospruebajuan
            SET name                        = COALESCE(:name, name),
                status                      = COALESCE(:status, status),
                archetype                   = COALESCE(:archetype, archetype),
                businessunit                = COALESCE(:businessunit, businessunit),
                lastedited                  = COALESCE(:lastedited, lastedited),
                campaigncount               = COALESCE(:campaigncount, campaigncount),
                type                        = COALESCE(:type, type),
                age                         = COALESCE(:age, age),
                locations                   = COALESCE(:locations, locations),
                education                   = COALESCE(:education, education),
                job                         = COALESCE(:job, job),
                income                      = COALESCE(:income, income),
                brandrelationship           = COALESCE(:brandrelationship, brandrelationship),
                digitalchannels             = COALESCE(:digitalchannels, digitalchannels),
                otherchannelslist           = COALESCE(:otherchannelslist, otherchannelslist),
                decisionmaking              = COALESCE(:decisionmaking, decisionmaking),
                currentactivity             = COALESCE(:currentactivity, currentactivity),
                satisfactionlevel           = COALESCE(:satisfactionlevel, satisfactionlevel),
                autonomylevel               = COALESCE(:autonomylevel, autonomylevel),
                teamsize                    = COALESCE(:teamsize, teamsize),
                dreamsvision                = COALESCE(:dreamsvision, dreamsvision),
                successfeeling              = COALESCE(:successfeeling, successfeeling),
                superficialpains            = COALESCE(:superficialpains, superficialpains),
                emotionalload               = COALESCE(:emotionalload, emotionalload),
                dailymanifestation          = COALESCE(:dailymanifestation, dailymanifestation),
                transformationcost          = COALESCE(:transformationcost, transformationcost),
                emotionalwound              = COALESCE(:emotionalwound, emotionalwound),
                previoussolutions           = COALESCE(:previoussolutions, previoussolutions),
                searchhistory               = COALESCE(:searchhistory, searchhistory),
                triggers                    = COALESCE(:triggers, triggers),
                objectives                  = COALESCE(:objectives, objectives),
                consciousnesslevel          = COALESCE(:consciousnesslevel, consciousnesslevel),
                narrativestyle              = COALESCE(:narrativestyle, narrativestyle),
                connectionstimulus          = COALESCE(:connectionstimulus, connectionstimulus),
                emotionalpurchasebehavior   = COALESCE(:emotionalpurchasebehavior, emotionalpurchasebehavior),
                narrativestory              = COALESCE(:narrativestory, narrativestory),
                after                       = COALESCE(:after, after),
                visualreflection            = COALESCE(:visualreflection, visualreflection),
                impactedbycampaign          = COALESCE(:impactedbycampaign, impactedbycampaign),
                campaignlinks               = COALESCE(:campaignlinks, campaignlinks)
            WHERE id = :id;
            """,
        id=id_usuario,
        **body
        )
    except Exception as e:
        print("Error al actualizar usuario:", repr(e))
        raise  # o convierte en return con error 500
    finally:
        conn.close()




# Funcion principal para activar la api
def lambda_handler(event, context):
    # Obtiene los datos de quien lo llama
    path = event.get("path", "")
    method = event.get("httpMethod", "")
    raw_body = event.get("body")

    # Verifica si obtuvo o no obtuvo informacion
    if raw_body is not None:
        body = json.loads(raw_body.strip())
    else:
        body = {}
    
    # obtiene la ruta desde el ultimo / que se encuentra
    ruta = event.get("resource")  # "/editar_usuario/{id}"

    # Endpoint para obtener la informacion de los usuarios
    if ruta == "/usuarios" and method == "GET":
        usuarios = listar_usuarios()
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization",
            },
            "body": json.dumps([asdict(u) for u in usuarios], default=lambda o: o.isoformat() if isinstance(o, datetime) else o)        
        }

    # Endpoint para guardar la informacion de los usuarios
    elif ruta == "/usuarios" and method == "POST":
        if body:
            body = json.loads(event.get("body"))
            insertaEnDB(body)
            return {
                "statusCode": 201,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "POST, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type, Authorization",
                },
                "body": json.dumps("Datos insertados correctamente")
            }



    elif ruta == "/usuarios/{usuario_id}" and method == "PUT":
        if body:
            body = json.loads(event.get("body"))
            id_usuario = event["pathParameters"]["usuario_id"]

            try:
                editarEnDB(id_usuario, body)
            except Exception as e:
                return {
                    "statusCode": 500,
                    "headers": {
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Methods": "OPTIONS, PUT",
                        "Access-Control-Allow-Headers": "Content-Type"
                    },
                    "body": json.dumps({"error": str(e)})
                }

            return {
                "statusCode": 202,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS, PUT",
                    "Access-Control-Allow-Headers": "Content-Type"
                },
                "body": json.dumps("Datos editados correctamente")
            }


    # Retorna si no se llama a ningun endpoint
    else:
        return {
            "statusCode": 404,
             "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "GET, POST, PUT, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type, Authorization",
            },   
            "body": "Endpoint no reconocido"
        }
