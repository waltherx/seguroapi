--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2023-10-03 21:57:41

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 3597 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- TOC entry 259 (class 1255 OID 98520)
-- Name: insertar_medico(integer, text, text, date, text, character, character, text, integer, text, text, text, integer); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.insertar_medico(IN p_ci integer, IN p_nombres text, IN p_apellidos text, IN p_fecha_nacimiento date, IN p_direccion text, IN p_genero character, IN p_estado_civil character, IN p_especialidad text, IN p_hospital_id integer, IN p_name_user text, IN p_password text, IN p_email text, IN p_id_rol integer)
    LANGUAGE plpgsql
    AS $$
begin
    begin
		
insert
	into
	persona (ci,
	nombres,
	apellidos,
	fecha_nacimiento ,
	direccion,
	genero,
	estado_civil)
values(p_ci,
p_nombres,
p_apellidos,
p_fecha_nacimiento,
p_direccion,
p_genero,
p_estado_civil);

insert
	into
	medico (especialidad,
	hospital_id,
	ci_persona)
values(p_especialidad ,
p_hospital_id,
p_ci);


insert
	into
	usuario (nameuser,
	"password",
	email,
	estado,
	"token",
	idrol,
	ci_persona)
values(p_name_user,
p_password,
p_email,
'act',
'',
p_id_rol,
p_ci);

raise notice 'Paciente agregado correctamente';

commit;

exception
when others then
            rollback;
raise;
end;
end;
$$;


ALTER PROCEDURE public.insertar_medico(IN p_ci integer, IN p_nombres text, IN p_apellidos text, IN p_fecha_nacimiento date, IN p_direccion text, IN p_genero character, IN p_estado_civil character, IN p_especialidad text, IN p_hospital_id integer, IN p_name_user text, IN p_password text, IN p_email text, IN p_id_rol integer) OWNER TO postgres;

--
-- TOC entry 260 (class 1255 OID 98521)
-- Name: verpersona(); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.verpersona()
    LANGUAGE plpgsql
    AS $$
begin
	select * from persona;
end;
$$;


ALTER PROCEDURE public.verpersona() OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 98522)
-- Name: alergia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alergia (
    idale integer NOT NULL,
    nombre character varying(120),
    descripcion text,
    gravedad character varying(150),
    reaccion character varying(150),
    paciente_id integer
);


ALTER TABLE public.alergia OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 98527)
-- Name: alergia_idale_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.alergia_idale_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.alergia_idale_seq OWNER TO postgres;

--
-- TOC entry 3598 (class 0 OID 0)
-- Dependencies: 215
-- Name: alergia_idale_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.alergia_idale_seq OWNED BY public.alergia.idale;


--
-- TOC entry 216 (class 1259 OID 98528)
-- Name: ambulancia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ambulancia (
    idam integer NOT NULL,
    modelo character varying(100) DEFAULT ''::character varying,
    marca character varying(100) DEFAULT ''::character varying,
    anio integer DEFAULT 0,
    placa character varying(10) DEFAULT ''::character varying,
    capcidad integer DEFAULT 0,
    lat numeric(10,8) DEFAULT '-17.84206900'::numeric,
    longi numeric(10,8) DEFAULT '-63.14662200'::numeric,
    estado character varying(1) DEFAULT 'f'::character varying
);


ALTER TABLE public.ambulancia OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 98539)
-- Name: ambulancia_idam_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ambulancia_idam_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ambulancia_idam_seq OWNER TO postgres;

--
-- TOC entry 3599 (class 0 OID 0)
-- Dependencies: 217
-- Name: ambulancia_idam_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ambulancia_idam_seq OWNED BY public.ambulancia.idam;


--
-- TOC entry 218 (class 1259 OID 98540)
-- Name: chofer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.chofer (
    idch integer NOT NULL,
    licencia character varying(20),
    categoria character varying(20),
    estado character varying(10),
    id_ambulancia integer,
    ci_persona integer
);


ALTER TABLE public.chofer OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 98543)
-- Name: chofer_idch_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.chofer_idch_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chofer_idch_seq OWNER TO postgres;

--
-- TOC entry 3600 (class 0 OID 0)
-- Dependencies: 219
-- Name: chofer_idch_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.chofer_idch_seq OWNED BY public.chofer.idch;


--
-- TOC entry 220 (class 1259 OID 98544)
-- Name: dispositivo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dispositivo (
    iddis integer NOT NULL,
    nombre character varying(100)
);


ALTER TABLE public.dispositivo OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 98547)
-- Name: dispositivo_iddis_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dispositivo_iddis_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dispositivo_iddis_seq OWNER TO postgres;

--
-- TOC entry 3601 (class 0 OID 0)
-- Dependencies: 221
-- Name: dispositivo_iddis_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dispositivo_iddis_seq OWNED BY public.dispositivo.iddis;


--
-- TOC entry 222 (class 1259 OID 98548)
-- Name: documento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.documento (
    iddoc integer NOT NULL,
    tipo character varying(150),
    url character varying(450),
    fecha timestamp without time zone NOT NULL,
    nombre character varying(200),
    paciente_id integer
);


ALTER TABLE public.documento OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 98553)
-- Name: documento_historial_clinico_iddoc_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.documento_historial_clinico_iddoc_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.documento_historial_clinico_iddoc_seq OWNER TO postgres;

--
-- TOC entry 3602 (class 0 OID 0)
-- Dependencies: 223
-- Name: documento_historial_clinico_iddoc_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.documento_historial_clinico_iddoc_seq OWNED BY public.documento.iddoc;


--
-- TOC entry 224 (class 1259 OID 98554)
-- Name: emergencia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.emergencia (
    idem integer NOT NULL,
    fecha timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    descripcion text,
    id_ambulancia integer,
    id_hospital integer,
    estado character varying(1) DEFAULT 'f'::character varying
);


ALTER TABLE public.emergencia OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 98561)
-- Name: emergencia_idem_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.emergencia_idem_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.emergencia_idem_seq OWNER TO postgres;

--
-- TOC entry 3603 (class 0 OID 0)
-- Dependencies: 225
-- Name: emergencia_idem_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.emergencia_idem_seq OWNED BY public.emergencia.idem;


--
-- TOC entry 226 (class 1259 OID 98562)
-- Name: enfermedad; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.enfermedad (
    idenf integer NOT NULL,
    nombre character varying(120) DEFAULT ''::character varying,
    descripcion text DEFAULT ''::text,
    causa text DEFAULT ''::text,
    sintoma text DEFAULT ''::text,
    diagnostico text DEFAULT ''::text,
    paciente_id integer
);


ALTER TABLE public.enfermedad OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 98572)
-- Name: enfermedad_idenf_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.enfermedad_idenf_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enfermedad_idenf_seq OWNER TO postgres;

--
-- TOC entry 3604 (class 0 OID 0)
-- Dependencies: 227
-- Name: enfermedad_idenf_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.enfermedad_idenf_seq OWNED BY public.enfermedad.idenf;


--
-- TOC entry 228 (class 1259 OID 98573)
-- Name: hospital; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hospital (
    idh integer NOT NULL,
    nombre character varying(150) NOT NULL,
    direccion character varying(250),
    lat numeric(10,8),
    longi numeric(10,8)
);


ALTER TABLE public.hospital OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 98576)
-- Name: hospital_idh_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.hospital_idh_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hospital_idh_seq OWNER TO postgres;

--
-- TOC entry 3605 (class 0 OID 0)
-- Dependencies: 229
-- Name: hospital_idh_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.hospital_idh_seq OWNED BY public.hospital.idh;


--
-- TOC entry 230 (class 1259 OID 98577)
-- Name: medicamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.medicamento (
    idme integer NOT NULL,
    nombre character varying(50) NOT NULL,
    descripcion text DEFAULT ''::text,
    cantidad integer DEFAULT 0,
    unidad_medida character varying(20) DEFAULT ''::character varying,
    paciente_id integer
);


ALTER TABLE public.medicamento OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 98585)
-- Name: medicamento_idme_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.medicamento_idme_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medicamento_idme_seq OWNER TO postgres;

--
-- TOC entry 3606 (class 0 OID 0)
-- Dependencies: 231
-- Name: medicamento_idme_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.medicamento_idme_seq OWNED BY public.medicamento.idme;


--
-- TOC entry 232 (class 1259 OID 98586)
-- Name: medico; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.medico (
    idmed integer NOT NULL,
    especialidad character varying(100),
    hospital_id integer,
    ci_persona integer
);


ALTER TABLE public.medico OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 98589)
-- Name: medico_idmed_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.medico_idmed_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medico_idmed_seq OWNER TO postgres;

--
-- TOC entry 3607 (class 0 OID 0)
-- Dependencies: 233
-- Name: medico_idmed_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.medico_idmed_seq OWNED BY public.medico.idmed;


--
-- TOC entry 234 (class 1259 OID 98590)
-- Name: notificacion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notificacion (
    idnoti integer NOT NULL,
    titulo text NOT NULL,
    descripcion text NOT NULL,
    fecha_creacion timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    fecha_envio timestamp without time zone,
    user_destino integer NOT NULL,
    user_remitente integer,
    leido boolean DEFAULT false NOT NULL
);


ALTER TABLE public.notificacion OWNER TO postgres;

--
-- TOC entry 235 (class 1259 OID 98597)
-- Name: notificacion_idnoti_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.notificacion_idnoti_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.notificacion_idnoti_seq OWNER TO postgres;

--
-- TOC entry 3608 (class 0 OID 0)
-- Dependencies: 235
-- Name: notificacion_idnoti_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.notificacion_idnoti_seq OWNED BY public.notificacion.idnoti;


--
-- TOC entry 236 (class 1259 OID 98598)
-- Name: operacion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.operacion (
    idop integer NOT NULL,
    tipo character varying(100) NOT NULL,
    fecha date NOT NULL,
    descripcion text,
    paciente_id integer
);


ALTER TABLE public.operacion OWNER TO postgres;

--
-- TOC entry 237 (class 1259 OID 98603)
-- Name: operacion_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.operacion_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.operacion_id_seq OWNER TO postgres;

--
-- TOC entry 3609 (class 0 OID 0)
-- Dependencies: 237
-- Name: operacion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.operacion_id_seq OWNED BY public.operacion.idop;


--
-- TOC entry 238 (class 1259 OID 98604)
-- Name: paciente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.paciente (
    idpac integer NOT NULL,
    tiposangre character varying(10),
    hipertencion character varying(5),
    altura numeric(5,2),
    peso numeric(5,2),
    ci_persona integer
);


ALTER TABLE public.paciente OWNER TO postgres;

--
-- TOC entry 239 (class 1259 OID 98607)
-- Name: paciente_idpac_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.paciente_idpac_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.paciente_idpac_seq OWNER TO postgres;

--
-- TOC entry 3610 (class 0 OID 0)
-- Dependencies: 239
-- Name: paciente_idpac_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.paciente_idpac_seq OWNED BY public.paciente.idpac;


--
-- TOC entry 240 (class 1259 OID 98608)
-- Name: paramedico; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.paramedico (
    idpar integer NOT NULL,
    especialidad character varying(50),
    id_ambulancia integer,
    ci_persona integer
);


ALTER TABLE public.paramedico OWNER TO postgres;

--
-- TOC entry 241 (class 1259 OID 98611)
-- Name: paramedico_idpar_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.paramedico_idpar_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.paramedico_idpar_seq OWNER TO postgres;

--
-- TOC entry 3611 (class 0 OID 0)
-- Dependencies: 241
-- Name: paramedico_idpar_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.paramedico_idpar_seq OWNED BY public.paramedico.idpar;


--
-- TOC entry 242 (class 1259 OID 98612)
-- Name: persona; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.persona (
    ci integer NOT NULL,
    nombres character varying(120) NOT NULL,
    apellidos character varying(200) NOT NULL,
    fecha_nacimiento date,
    foto_url character varying(500) DEFAULT 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685674650/perfil/perfiluserdefault_ax7rd1.png'::character varying,
    foto_name character varying(99),
    direccion character varying(150),
    genero character varying(20) NOT NULL,
    estado_civil character varying(20) NOT NULL
);


ALTER TABLE public.persona OWNER TO postgres;

--
-- TOC entry 243 (class 1259 OID 98618)
-- Name: phone; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.phone (
    idp integer NOT NULL,
    numero character varying(12),
    referencia character varying(120),
    ci_persona integer
);


ALTER TABLE public.phone OWNER TO postgres;

--
-- TOC entry 244 (class 1259 OID 98621)
-- Name: phone_idp_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.phone_idp_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.phone_idp_seq OWNER TO postgres;

--
-- TOC entry 3612 (class 0 OID 0)
-- Dependencies: 244
-- Name: phone_idp_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.phone_idp_seq OWNED BY public.phone.idp;


--
-- TOC entry 245 (class 1259 OID 98622)
-- Name: rol; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rol (
    idrol integer NOT NULL,
    nombre character varying(45)
);


ALTER TABLE public.rol OWNER TO postgres;

--
-- TOC entry 246 (class 1259 OID 98625)
-- Name: rol_idrol_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.rol_idrol_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rol_idrol_seq OWNER TO postgres;

--
-- TOC entry 3613 (class 0 OID 0)
-- Dependencies: 246
-- Name: rol_idrol_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.rol_idrol_seq OWNED BY public.rol.idrol;


--
-- TOC entry 247 (class 1259 OID 98626)
-- Name: siniestro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.siniestro (
    ids integer NOT NULL,
    descripcion character varying(350),
    fecha timestamp without time zone,
    lat numeric(10,8),
    longi numeric(10,8),
    paciente_id integer
);


ALTER TABLE public.siniestro OWNER TO postgres;

--
-- TOC entry 248 (class 1259 OID 98629)
-- Name: siniestro_ids_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.siniestro_ids_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.siniestro_ids_seq OWNER TO postgres;

--
-- TOC entry 3614 (class 0 OID 0)
-- Dependencies: 248
-- Name: siniestro_ids_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.siniestro_ids_seq OWNED BY public.siniestro.ids;


--
-- TOC entry 249 (class 1259 OID 98630)
-- Name: tokens; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tokens (
    idt integer NOT NULL,
    user_id integer NOT NULL,
    token character varying(355) NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone
);


ALTER TABLE public.tokens OWNER TO postgres;

--
-- TOC entry 250 (class 1259 OID 98634)
-- Name: tokens_idt_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tokens_idt_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tokens_idt_seq OWNER TO postgres;

--
-- TOC entry 3615 (class 0 OID 0)
-- Dependencies: 250
-- Name: tokens_idt_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tokens_idt_seq OWNED BY public.tokens.idt;


--
-- TOC entry 251 (class 1259 OID 98635)
-- Name: tratamiento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tratamiento (
    idtra integer NOT NULL,
    fecha_inicio date NOT NULL,
    fecha_fin date,
    descripcion text,
    idenf integer
);


ALTER TABLE public.tratamiento OWNER TO postgres;

--
-- TOC entry 252 (class 1259 OID 98640)
-- Name: tratamiento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tratamiento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tratamiento_id_seq OWNER TO postgres;

--
-- TOC entry 3616 (class 0 OID 0)
-- Dependencies: 252
-- Name: tratamiento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tratamiento_id_seq OWNED BY public.tratamiento.idtra;


--
-- TOC entry 253 (class 1259 OID 98641)
-- Name: ubicacion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ubicacion (
    idubi integer NOT NULL,
    latitud numeric(9,6),
    longitud numeric(9,6),
    hora timestamp without time zone DEFAULT now(),
    persona_ci integer,
    dispositivo_id integer
);


ALTER TABLE public.ubicacion OWNER TO postgres;

--
-- TOC entry 254 (class 1259 OID 98645)
-- Name: ubicacion_idubi_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ubicacion_idubi_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ubicacion_idubi_seq OWNER TO postgres;

--
-- TOC entry 3617 (class 0 OID 0)
-- Dependencies: 254
-- Name: ubicacion_idubi_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ubicacion_idubi_seq OWNED BY public.ubicacion.idubi;


--
-- TOC entry 255 (class 1259 OID 98646)
-- Name: usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario (
    idu integer NOT NULL,
    nameuser character varying(45) NOT NULL,
    password character varying(150) NOT NULL,
    email character varying(45) NOT NULL,
    estado character varying(5) DEFAULT 'act'::character varying NOT NULL,
    token character varying(250),
    idrol integer,
    ci_persona integer
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- TOC entry 256 (class 1259 OID 98652)
-- Name: usuario_idu_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuario_idu_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usuario_idu_seq OWNER TO postgres;

--
-- TOC entry 3618 (class 0 OID 0)
-- Dependencies: 256
-- Name: usuario_idu_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuario_idu_seq OWNED BY public.usuario.idu;


--
-- TOC entry 257 (class 1259 OID 98653)
-- Name: vacuna; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vacuna (
    idvac integer NOT NULL,
    nombre character varying(50) NOT NULL,
    dosis_requeridas integer,
    paciente_id integer
);


ALTER TABLE public.vacuna OWNER TO postgres;

--
-- TOC entry 258 (class 1259 OID 98656)
-- Name: vacuna_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vacuna_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vacuna_id_seq OWNER TO postgres;

--
-- TOC entry 3619 (class 0 OID 0)
-- Dependencies: 258
-- Name: vacuna_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vacuna_id_seq OWNED BY public.vacuna.idvac;


--
-- TOC entry 3284 (class 2604 OID 98850)
-- Name: alergia idale; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alergia ALTER COLUMN idale SET DEFAULT nextval('public.alergia_idale_seq'::regclass);


--
-- TOC entry 3285 (class 2604 OID 98851)
-- Name: ambulancia idam; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ambulancia ALTER COLUMN idam SET DEFAULT nextval('public.ambulancia_idam_seq'::regclass);


--
-- TOC entry 3294 (class 2604 OID 98852)
-- Name: chofer idch; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chofer ALTER COLUMN idch SET DEFAULT nextval('public.chofer_idch_seq'::regclass);


--
-- TOC entry 3295 (class 2604 OID 98853)
-- Name: dispositivo iddis; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispositivo ALTER COLUMN iddis SET DEFAULT nextval('public.dispositivo_iddis_seq'::regclass);


--
-- TOC entry 3296 (class 2604 OID 98854)
-- Name: documento iddoc; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.documento ALTER COLUMN iddoc SET DEFAULT nextval('public.documento_historial_clinico_iddoc_seq'::regclass);


--
-- TOC entry 3297 (class 2604 OID 98855)
-- Name: emergencia idem; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emergencia ALTER COLUMN idem SET DEFAULT nextval('public.emergencia_idem_seq'::regclass);


--
-- TOC entry 3300 (class 2604 OID 98856)
-- Name: enfermedad idenf; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enfermedad ALTER COLUMN idenf SET DEFAULT nextval('public.enfermedad_idenf_seq'::regclass);


--
-- TOC entry 3306 (class 2604 OID 98857)
-- Name: hospital idh; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hospital ALTER COLUMN idh SET DEFAULT nextval('public.hospital_idh_seq'::regclass);


--
-- TOC entry 3307 (class 2604 OID 98858)
-- Name: medicamento idme; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medicamento ALTER COLUMN idme SET DEFAULT nextval('public.medicamento_idme_seq'::regclass);


--
-- TOC entry 3311 (class 2604 OID 98859)
-- Name: medico idmed; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medico ALTER COLUMN idmed SET DEFAULT nextval('public.medico_idmed_seq'::regclass);


--
-- TOC entry 3312 (class 2604 OID 98860)
-- Name: notificacion idnoti; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notificacion ALTER COLUMN idnoti SET DEFAULT nextval('public.notificacion_idnoti_seq'::regclass);


--
-- TOC entry 3315 (class 2604 OID 98861)
-- Name: operacion idop; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operacion ALTER COLUMN idop SET DEFAULT nextval('public.operacion_id_seq'::regclass);


--
-- TOC entry 3316 (class 2604 OID 98862)
-- Name: paciente idpac; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paciente ALTER COLUMN idpac SET DEFAULT nextval('public.paciente_idpac_seq'::regclass);


--
-- TOC entry 3317 (class 2604 OID 98863)
-- Name: paramedico idpar; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paramedico ALTER COLUMN idpar SET DEFAULT nextval('public.paramedico_idpar_seq'::regclass);


--
-- TOC entry 3319 (class 2604 OID 98864)
-- Name: phone idp; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone ALTER COLUMN idp SET DEFAULT nextval('public.phone_idp_seq'::regclass);


--
-- TOC entry 3320 (class 2604 OID 98865)
-- Name: rol idrol; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rol ALTER COLUMN idrol SET DEFAULT nextval('public.rol_idrol_seq'::regclass);


--
-- TOC entry 3321 (class 2604 OID 98866)
-- Name: siniestro ids; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.siniestro ALTER COLUMN ids SET DEFAULT nextval('public.siniestro_ids_seq'::regclass);


--
-- TOC entry 3322 (class 2604 OID 98867)
-- Name: tokens idt; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tokens ALTER COLUMN idt SET DEFAULT nextval('public.tokens_idt_seq'::regclass);


--
-- TOC entry 3324 (class 2604 OID 98868)
-- Name: tratamiento idtra; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tratamiento ALTER COLUMN idtra SET DEFAULT nextval('public.tratamiento_id_seq'::regclass);


--
-- TOC entry 3325 (class 2604 OID 98869)
-- Name: ubicacion idubi; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ubicacion ALTER COLUMN idubi SET DEFAULT nextval('public.ubicacion_idubi_seq'::regclass);


--
-- TOC entry 3327 (class 2604 OID 98870)
-- Name: usuario idu; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario ALTER COLUMN idu SET DEFAULT nextval('public.usuario_idu_seq'::regclass);


--
-- TOC entry 3329 (class 2604 OID 98871)
-- Name: vacuna idvac; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacuna ALTER COLUMN idvac SET DEFAULT nextval('public.vacuna_id_seq'::regclass);


--
-- TOC entry 3547 (class 0 OID 98522)
-- Dependencies: 214
-- Data for Name: alergia; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.alergia VALUES (32, 'Picaduras de insectos', '', '', '', 1);
INSERT INTO public.alergia VALUES (33, 'gelatina', '', 'leve', '', 25);
INSERT INTO public.alergia VALUES (30, 'cafe negro', 'normal', 'intermedio-leve', 'fiebre ocasional', 9);
INSERT INTO public.alergia VALUES (40, 'mandarina', 'fruta ', 'leve', '', 9);
INSERT INTO public.alergia VALUES (31, 'Mani', '', 'leve', '', 1);
INSERT INTO public.alergia VALUES (6, 'sodio', NULL, NULL, NULL, 4);
INSERT INTO public.alergia VALUES (7, 'galleta', NULL, NULL, NULL, 2);
INSERT INTO public.alergia VALUES (11, 'Sal', NULL, NULL, NULL, 5);
INSERT INTO public.alergia VALUES (12, 'Croqueta', NULL, NULL, NULL, 6);
INSERT INTO public.alergia VALUES (13, 'Coco', NULL, NULL, NULL, 7);
INSERT INTO public.alergia VALUES (1, 'Polvo ', NULL, NULL, NULL, 5);
INSERT INTO public.alergia VALUES (9, 'Pelo de gato', NULL, NULL, NULL, 4);
INSERT INTO public.alergia VALUES (10, 'Pelo', NULL, 'leve', 'ardor', 3);
INSERT INTO public.alergia VALUES (5, 'plastico', NULL, 'medio', 'Irritacion en la piel', 3);
INSERT INTO public.alergia VALUES (14, 'miel de abeja', 'tia', 'leve', 'ardor en la piel', 4);
INSERT INTO public.alergia VALUES (15, 'miel de abeja', 'tia', '', 'ardor en la piel', 5);
INSERT INTO public.alergia VALUES (20, 'Galleta de avena', '', '', '', 2);
INSERT INTO public.alergia VALUES (23, 'Sol', '', 'leve', 'piel reseca', 2);
INSERT INTO public.alergia VALUES (24, 'gatos', 'el pelo de gato', 'media', '', 2);
INSERT INTO public.alergia VALUES (26, 'grasa', 'de vehiculos', '', '', 5);
INSERT INTO public.alergia VALUES (27, 'Penicilina', '', '', '', 1);
INSERT INTO public.alergia VALUES (28, 'polvo', 'arena', '', '', 17);
INSERT INTO public.alergia VALUES (29, 'Carton de papel', '', '', '', 6);


--
-- TOC entry 3549 (class 0 OID 98528)
-- Dependencies: 216
-- Data for Name: ambulancia; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.ambulancia VALUES (2, 'GS125', 'NISSAN', 2020, '4040DSA', 5, -17.78470800, -63.18112200, 'f');
INSERT INTO public.ambulancia VALUES (3, 'Ford Transit Ambulance', 'Ford', 2013, '4433DSS', 7, -17.84206900, -63.14662200, 'f');
INSERT INTO public.ambulancia VALUES (9, 'Modelo P', 'Tesla', 2020, 'JKHD202', 7, -17.84206900, -63.14662200, 'f');
INSERT INTO public.ambulancia VALUES (11, 'EXPERT', '', 2014, 'DSO4577', 12, -17.84206900, -63.14662200, 'f');
INSERT INTO public.ambulancia VALUES (10, 'M1', 'Mazda', 2002, 'JFGG454', 5, -17.84206900, -63.14662200, 'f');
INSERT INTO public.ambulancia VALUES (1, 'F50', 'Ford', 2012, '2232ASS', 3, -17.84206900, -63.14662200, 'f');


--
-- TOC entry 3551 (class 0 OID 98540)
-- Dependencies: 218
-- Data for Name: chofer; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.chofer VALUES (4, '466664', 'C', 'OCUPADO', 2, 8931237);
INSERT INTO public.chofer VALUES (5, '456654', 'B', 'LIBRE', 1, 8155645);
INSERT INTO public.chofer VALUES (1, '465465', 'C', 'OCUPADO', 1, 8931234);
INSERT INTO public.chofer VALUES (2, '416525', 'B', 'OCUPADO', 2, 8931235);
INSERT INTO public.chofer VALUES (3, '465666', 'B', 'OCUPADO', 1, 8931236);
INSERT INTO public.chofer VALUES (6, '455251', 'C', 'LIBRE', 2, 8155654);


--
-- TOC entry 3553 (class 0 OID 98544)
-- Dependencies: 220
-- Data for Name: dispositivo; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.dispositivo VALUES (1, 'Xiaomi p1');
INSERT INTO public.dispositivo VALUES (2, 'Iphone 14');
INSERT INTO public.dispositivo VALUES (3, 'Samsung S21');


--
-- TOC entry 3555 (class 0 OID 98548)
-- Dependencies: 222
-- Data for Name: documento; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.documento VALUES (3, 'Rayos X', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1680995661/doc/1680995660-3FFP3WE7W1HT1512037282288.png.png', '2002-02-02 00:00:00', '1680995660-3FFP3WE7W1HT1512037282288.png.png', 2);
INSERT INTO public.documento VALUES (6, 'Informe de prueba cardíaca', NULL, '2023-05-09 03:01:06.712526', NULL, 3);
INSERT INTO public.documento VALUES (7, 'Nota de seguimiento', NULL, '2023-05-09 03:01:06.847179', NULL, 3);
INSERT INTO public.documento VALUES (8, 'Resultados de análisis', NULL, '2023-05-09 03:01:07.270276', NULL, 3);
INSERT INTO public.documento VALUES (9, 'Informes de prueba de función pulmonar', NULL, '2023-05-09 03:01:07.440063', NULL, 2);
INSERT INTO public.documento VALUES (10, 'Radiografia', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1680995661/doc/1680995660-3FFP3WE7W1HT1512037282288.png.png', '2023-05-09 11:43:57.474854', NULL, 8);
INSERT INTO public.documento VALUES (11, 'Certificadode Discapasidad', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1680995661/doc/1680995660-3FFP3WE7W1HT1512037282288.png.png', '2023-05-09 11:43:57.618953', NULL, 8);
INSERT INTO public.documento VALUES (4, 'Certificadode Discapasidad', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1680995661/doc/1680995660-3FFP3WE7W1HT1512037282288.png.png', '1994-08-05 00:00:00', '1680995660-3FFP3WE7W1HT1512037282288.png.png', 2);
INSERT INTO public.documento VALUES (1, 'Radiografia', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685116349/doc/radiografia_torax_fn2zfi.jpg', '2021-03-02 00:00:00', '1680995660-3FFP3WE7W1HT1512037282288.png.png', 1);
INSERT INTO public.documento VALUES (2, 'Carnet de Vacuna', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685116347/doc/carnet_de_vacuna_vckv3r.png', '2024-08-02 00:00:00', '1680995660-3FFP3WE7W1HT1512037282288.png.png', 1);
INSERT INTO public.documento VALUES (16, 'rayos gama', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685137606/doc/20230526_174644_PbPOP.jpg', '2023-05-26 21:46:47.340498', 'doc/20230526_174644_PbPOP', 4);
INSERT INTO public.documento VALUES (17, 'rayos x', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685161131/doc/20230527_001849_3Gunc.jpg', '2023-05-27 04:18:52.302207', 'doc/20230527_001849_3Gunc', 17);
INSERT INTO public.documento VALUES (18, 'rayos x', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685161922/doc/20230527_003200_vSaWE.jpg', '2023-05-27 04:32:03.787851', 'doc/20230527_003200_vSaWE', 17);
INSERT INTO public.documento VALUES (19, 'dsa', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685162223/doc/20230527_003703_W4VqU.png', '2023-05-27 04:37:04.902534', 'doc/20230527_003703_W4VqU', 17);
INSERT INTO public.documento VALUES (20, 'dsadsa', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685162258/doc/20230527_003728_i4JzX.jpg', '2023-05-27 04:37:39.561316', 'doc/20230527_003728_i4JzX', 17);
INSERT INTO public.documento VALUES (21, 'dsad', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685162317/doc/20230527_003836_M6gz2.jpg', '2023-05-27 04:38:38.860643', 'doc/20230527_003836_M6gz2', 17);
INSERT INTO public.documento VALUES (22, 'fweewds ds dsa das', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685162407/doc/20230527_004006_qeLTp.png', '2023-05-27 04:40:08.362799', 'doc/20230527_004006_qeLTp', 17);
INSERT INTO public.documento VALUES (23, 'pie', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685312964/doc/20230528_182921_qMmMq.png', '2023-05-28 22:29:25.983665', 'doc/20230528_182921_qMmMq', 6);
INSERT INTO public.documento VALUES (24, 'dsddd', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685312998/doc/20230528_182957_U17h7.png', '2023-05-28 22:29:59.683289', 'doc/20230528_182957_U17h7', 6);
INSERT INTO public.documento VALUES (25, 'Hemograma', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685509906/doc/20230531_051146_BVARV.jpg', '2023-05-31 05:11:47.073487', 'doc/20230531_051146_BVARV', 1);


--
-- TOC entry 3557 (class 0 OID 98554)
-- Dependencies: 224
-- Data for Name: emergencia; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.emergencia VALUES (2, '2023-04-21 19:56:06.563393', 'ds', 2, 2, 'v');
INSERT INTO public.emergencia VALUES (4, '2023-04-21 20:10:49.092136', 'sadsad', 2, 2, 'v');
INSERT INTO public.emergencia VALUES (5, '2023-04-21 20:12:21.966549', 'jsjsjsj', 2, 1, 'v');
INSERT INTO public.emergencia VALUES (62, '2023-05-19 21:47:05.02222', 'Nos dirigimos al hospital Clinica Incor', 1, 4, 'f');
INSERT INTO public.emergencia VALUES (63, '2023-05-31 03:42:41.973685', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (1, '2023-04-21 15:09:38.555297', 'PIE ROTO', 1, 1, 'f');
INSERT INTO public.emergencia VALUES (6, '2023-04-26 17:20:44.588422', 'Nos dirigimos al hospital Clinica Incor', 1, 4, 'v');
INSERT INTO public.emergencia VALUES (64, '2023-05-31 03:45:09.394198', 'Nos dirigimos al hospital Caja petrolera', 1, 2, 'v');
INSERT INTO public.emergencia VALUES (7, '2023-04-26 20:14:40.327833', 'Nos dirigimos al hospital Clinica Incor', 1, 4, 'v');
INSERT INTO public.emergencia VALUES (3, '2023-04-21 20:09:33.673786', 'no ta mal', 2, 2, 'f');
INSERT INTO public.emergencia VALUES (8, '2023-05-03 20:35:46.99811', 'Nos dirigimos al hospital Hospital Japones', 1, 3, 'v');
INSERT INTO public.emergencia VALUES (9, '2023-05-04 02:41:03.209205', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (10, '2023-05-09 20:30:35.735488', 'Nos dirigimos al hospital Caja petrolera', 1, 2, 'v');
INSERT INTO public.emergencia VALUES (11, '2023-05-09 20:31:09.752278', 'Nos dirigimos al hospital Caja petrolera', 2, 2, 'v');
INSERT INTO public.emergencia VALUES (12, '2023-05-09 20:44:56.550212', 'Nos dirigimos al hospital Clinica Melendre', 2, 7, 'v');
INSERT INTO public.emergencia VALUES (13, '2023-05-16 16:57:03.330475', 'Nos dirigimos al hospital Clinica Melendre', 1, 7, 'v');
INSERT INTO public.emergencia VALUES (14, '2023-05-16 16:57:08.341952', 'Nos dirigimos al hospital Clinica Melendre', 1, 7, 'v');
INSERT INTO public.emergencia VALUES (15, '2023-05-16 16:57:11.142187', 'Nos dirigimos al hospital Clinica Melendre', 1, 7, 'v');
INSERT INTO public.emergencia VALUES (16, '2023-05-16 16:58:20.254017', 'Nos dirigimos al hospital Caja petrolera', 1, 2, 'v');
INSERT INTO public.emergencia VALUES (17, '2023-05-16 16:58:22.621627', 'Nos dirigimos al hospital Caja petrolera', 1, 2, 'v');
INSERT INTO public.emergencia VALUES (18, '2023-05-16 16:58:23.137794', 'Nos dirigimos al hospital Caja petrolera', 1, 2, 'v');
INSERT INTO public.emergencia VALUES (19, '2023-05-16 16:58:23.359617', 'Nos dirigimos al hospital Caja petrolera', 1, 2, 'v');
INSERT INTO public.emergencia VALUES (20, '2023-05-16 16:58:23.503648', 'Nos dirigimos al hospital Caja petrolera', 1, 2, 'v');
INSERT INTO public.emergencia VALUES (21, '2023-05-16 16:59:06.555039', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (22, '2023-05-16 17:43:04.097251', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (23, '2023-05-16 17:48:17.280816', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (24, '2023-05-16 17:48:45.98165', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (25, '2023-05-16 17:49:06.403244', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (26, '2023-05-16 17:50:04.243612', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (27, '2023-05-16 17:50:10.771925', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (28, '2023-05-16 17:50:34.674568', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (29, '2023-05-16 17:50:54.079501', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (30, '2023-05-16 17:52:11.751993', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (31, '2023-05-16 17:52:41.929599', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (32, '2023-05-16 17:52:46.012448', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (33, '2023-05-16 17:52:49.395997', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (34, '2023-05-16 17:53:04.5858', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (35, '2023-05-16 17:53:10.60739', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (36, '2023-05-16 17:53:19.824704', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (37, '2023-05-16 17:53:22.969693', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (38, '2023-05-16 17:53:24.308673', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (39, '2023-05-16 17:53:26.087617', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (40, '2023-05-16 17:53:26.319565', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (41, '2023-05-16 17:53:26.625049', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (42, '2023-05-16 17:53:26.768591', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (43, '2023-05-16 17:53:26.916639', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (44, '2023-05-16 17:53:27.097488', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (45, '2023-05-16 17:53:30.08891', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (46, '2023-05-16 17:53:30.486797', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (47, '2023-05-16 17:53:30.504932', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (48, '2023-05-16 17:53:30.583837', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (49, '2023-05-16 17:53:30.862291', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'v');
INSERT INTO public.emergencia VALUES (50, '2023-05-16 18:11:33.919734', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (51, '2023-05-16 18:12:19.552635', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (52, '2023-05-16 18:12:19.857525', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (53, '2023-05-16 18:12:37.413882', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (54, '2023-05-16 18:14:03.957263', 'Nos dirigimos al hospital Clinica Incor', 1, 4, 'v');
INSERT INTO public.emergencia VALUES (55, '2023-05-16 18:22:20.954181', 'Nos dirigimos al hospital Clinica Incor', 1, 4, 'v');
INSERT INTO public.emergencia VALUES (56, '2023-05-16 21:15:24.920218', 'Nos dirigimos al hospital Clinica Melendre', 1, 7, 'v');
INSERT INTO public.emergencia VALUES (57, '2023-05-16 21:16:12.036655', 'Nos dirigimos al hospital Caja petrolera', 1, 2, 'v');
INSERT INTO public.emergencia VALUES (58, '2023-05-16 21:16:28.331828', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'f');
INSERT INTO public.emergencia VALUES (59, '2023-05-16 21:18:38.225403', 'Nos dirigimos al hospital Caja petrolera', 1, 2, 'f');
INSERT INTO public.emergencia VALUES (60, '2023-05-19 21:32:29.627616', 'Nos dirigimos al hospital Clinica Melendre', 1, 7, 'f');
INSERT INTO public.emergencia VALUES (61, '2023-05-19 21:36:20.920882', 'Nos dirigimos al hospital Clinica Melendre', 1, 7, 'f');
INSERT INTO public.emergencia VALUES (65, '2023-05-31 03:45:24.665747', 'Nos dirigimos al hospital Hospital Japones', 1, 3, 'v');
INSERT INTO public.emergencia VALUES (66, '2023-05-31 03:45:35.835143', 'Nos dirigimos al hospital Clinica Incor', 1, 4, 'v');
INSERT INTO public.emergencia VALUES (67, '2023-05-31 03:45:44.968795', 'Nos dirigimos al hospital Hospital de Ninios', 1, 5, 'v');
INSERT INTO public.emergencia VALUES (68, '2023-05-31 03:45:57.851777', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'v');
INSERT INTO public.emergencia VALUES (69, '2023-05-31 03:46:13.000602', 'Nos dirigimos al hospital Clinica Melendre', 1, 7, 'v');
INSERT INTO public.emergencia VALUES (70, '2023-05-31 04:30:15.097735', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'f');
INSERT INTO public.emergencia VALUES (71, '2023-05-31 04:35:37.338056', 'Nos dirigimos al hospital Hospital Japones', 1, 3, 'f');
INSERT INTO public.emergencia VALUES (72, '2023-05-31 04:38:07.993075', 'Nos dirigimos al hospital Hospital San Juan de Dios', 1, 6, 'f');
INSERT INTO public.emergencia VALUES (73, '2023-05-31 04:40:57.863099', 'Nos dirigimos al hospital Caja petrolera', 1, 2, 'f');
INSERT INTO public.emergencia VALUES (74, '2023-05-31 04:44:03.959344', 'Nos dirigimos al hospital Clinica Incor', 1, 4, 'f');
INSERT INTO public.emergencia VALUES (75, '2023-05-31 04:50:26.382578', 'Nos dirigimos al hospital Hospital de Ninios', 1, 5, 'f');
INSERT INTO public.emergencia VALUES (76, '2023-05-31 04:52:51.532235', 'Nos dirigimos al hospital Clinica Melendre', 1, 7, 'f');
INSERT INTO public.emergencia VALUES (77, '2023-05-31 05:01:00.583056', 'Nos dirigimos al hospital Hospital Japones', 1, 3, 'f');
INSERT INTO public.emergencia VALUES (78, '2023-06-02 01:43:23.641421', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'f');
INSERT INTO public.emergencia VALUES (79, '2023-06-05 20:21:40.495253', 'Nos dirigimos al hospital Clinica Incor', 2, 4, 'v');
INSERT INTO public.emergencia VALUES (80, '2023-06-07 13:35:48.884925', 'Nos dirigimos al hospital Hospital De La Mujer Dr. Percy Boland', 1, 1, 'f');


--
-- TOC entry 3559 (class 0 OID 98562)
-- Dependencies: 226
-- Data for Name: enfermedad; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.enfermedad VALUES (3, 'Gastritis', '', '', '', '', 1);
INSERT INTO public.enfermedad VALUES (32, 'Tos', '', 'frio', '', '', 9);
INSERT INTO public.enfermedad VALUES (43, 'Fiebre', '', 'frio', '', '', 9);
INSERT INTO public.enfermedad VALUES (6, 'Diabetes', 'enfermedad de base', ' ', '', '', 1);
INSERT INTO public.enfermedad VALUES (34, 'fiebre', '40 grados de temperatura coorporal', 'expuesto a bajas temperaturas', '', 'descanso ', 11);
INSERT INTO public.enfermedad VALUES (19, 'Artritis', 'una enfermedad inflamatoria que causa dolor, inflamación y rigidez en las articulaciones.', NULL, NULL, NULL, 5);
INSERT INTO public.enfermedad VALUES (20, 'Enfermedad celíaca', 'una enfermedad autoinmune en la que el cuerpo no puede tolerar el gluten, lo que puede causar daño al intestino delgado.', NULL, NULL, NULL, 4);
INSERT INTO public.enfermedad VALUES (21, 'Infección urinaria', 'una infección bacteriana que afecta el tracto urinario y puede causar dolor al orinar, necesidad frecuente de orinar y fiebre.', NULL, NULL, NULL, 2);
INSERT INTO public.enfermedad VALUES (22, 'Asma', 'una enfermedad crónica que afecta las vías respiratorias y causa dificultad para respirar.', NULL, NULL, NULL, 2);
INSERT INTO public.enfermedad VALUES (23, 'Artritis', 'una enfermedad inflamatoria que causa dolor, inflamación y rigidez en las articulaciones.', NULL, NULL, NULL, 3);
INSERT INTO public.enfermedad VALUES (13, 'Gripe', '', '', NULL, NULL, 2);
INSERT INTO public.enfermedad VALUES (7, 'calambre', '', '', NULL, NULL, 4);
INSERT INTO public.enfermedad VALUES (8, 'migraña', '', '', NULL, NULL, 5);
INSERT INTO public.enfermedad VALUES (17, 'piedra riñon', '', '', NULL, NULL, 7);
INSERT INTO public.enfermedad VALUES (26, 'dengue emorragico', '', 'viaje a campo cotoca', '', '', 3);
INSERT INTO public.enfermedad VALUES (25, 'Fiebre alta', 'enfermedad viral', '', '', '', 3);
INSERT INTO public.enfermedad VALUES (2, 'Tos seca', '', '', '', '', 3);
INSERT INTO public.enfermedad VALUES (24, 'Tos seca', '', '', '', '', 3);
INSERT INTO public.enfermedad VALUES (18, 'Diabetes', 'una enfermedad crónica en la que los niveles de azúcar en la sangre son anormalmente altos, lo que puede causar daño a los vasos sanguíneos y otros órganos.', 'azucar', 'agotamiento, sueño', 'Tratamiento ', 6);
INSERT INTO public.enfermedad VALUES (30, 'Tos seca', '', 'Expuesto ala lluvia', 'flema, cansancio', '', 6);
INSERT INTO public.enfermedad VALUES (31, 'Caida Fractura', 'huesos lesionados dela espalda', 'accidente', 'dolor, emorragia', 'reposo', 6);


--
-- TOC entry 3561 (class 0 OID 98573)
-- Dependencies: 228
-- Data for Name: hospital; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.hospital VALUES (2, 'Caja petrolera', '5to anillo', -17.78953250, -63.18260937);
INSERT INTO public.hospital VALUES (7, 'Clinica Melendre', '5to anillo', -17.80328820, -63.19909027);
INSERT INTO public.hospital VALUES (3, 'Hospital Japones', '3ro anillo', -17.77315150, -63.15502769);
INSERT INTO public.hospital VALUES (4, 'Clinica Incor', '5to anillo', -17.78804610, -63.19518650);
INSERT INTO public.hospital VALUES (6, 'Hospital San Juan de Dios', '8ro anillo', -17.77851684, -63.18592606);
INSERT INTO public.hospital VALUES (1, 'Hospital De La Mujer Dr. Percy Boland', '5to anillo', -17.77839882, -63.18721220);
INSERT INTO public.hospital VALUES (5, 'Hospital de Ninios', 'tro anillo', -17.78077464, -63.18652687);


--
-- TOC entry 3563 (class 0 OID 98577)
-- Dependencies: 230
-- Data for Name: medicamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.medicamento VALUES (1, 'Paracetamol', 'para la fiebre', 1, '8xh', 1);
INSERT INTO public.medicamento VALUES (2, 'Novadol', 'Dolor de cuerpo', 2, '', 2);
INSERT INTO public.medicamento VALUES (3, 'Vitamin', 'refuerzos', 2, 'c/ 6h', 2);
INSERT INTO public.medicamento VALUES (4, 'Pomada quemadura', 'calmante', 2, 'c/ 6h', 1);
INSERT INTO public.medicamento VALUES (5, 'vitamia A', 'vitamina', 1, '10 pm', 2);
INSERT INTO public.medicamento VALUES (6, 'Ramipril', 'hipertencion', 3, 'cada 8h', 3);
INSERT INTO public.medicamento VALUES (7, 'Aspirina', 'casi para todo', 2, 'noches', 3);
INSERT INTO public.medicamento VALUES (8, 'Amlodipina', 'la angina', 5, 'diario', 3);
INSERT INTO public.medicamento VALUES (10, 'paracetamol new', 'Para migraña fuerte', 0, '2 al dia', 5);
INSERT INTO public.medicamento VALUES (11, 'bacterol', 'n/d', 4, 'ml', 9);
INSERT INTO public.medicamento VALUES (27, 'Paracetamol', 'pastillas', 3, 'ml', 9);
INSERT INTO public.medicamento VALUES (21, 'Nobadol', '', 5, '2 ml', 9);


--
-- TOC entry 3565 (class 0 OID 98586)
-- Dependencies: 232
-- Data for Name: medico; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.medico VALUES (1, 'Fisioterapia', 1, 8931239);
INSERT INTO public.medico VALUES (4, 'Ginecología', 4, 8931242);
INSERT INTO public.medico VALUES (2, 'Dermatologia', 2, 8931240);
INSERT INTO public.medico VALUES (3, 'Ortopedia', 3, 8931241);
INSERT INTO public.medico VALUES (5, 'Ortopedia', 5, 8989871);
INSERT INTO public.medico VALUES (6, 'Dentista', 6, 8989872);
INSERT INTO public.medico VALUES (7, 'Psiquiatra', 7, 8989873);
INSERT INTO public.medico VALUES (8, 'pass', 1, 8155654);
INSERT INTO public.medico VALUES (15, 'pass', 1, 665878);
INSERT INTO public.medico VALUES (16, 'pass', 1, 6658732);
INSERT INTO public.medico VALUES (18, 'pass', 1, 665822);
INSERT INTO public.medico VALUES (19, 'dsadsa', 4, 8765401);
INSERT INTO public.medico VALUES (20, 'wqqw', 1, 8765000);
INSERT INTO public.medico VALUES (22, 'ginicologia', 4, 1234);
INSERT INTO public.medico VALUES (21, 'Nefrología', 5, 432432);
INSERT INTO public.medico VALUES (23, 'Dixlexia', 6, 365254);
INSERT INTO public.medico VALUES (24, 'General', 1, 55699);
INSERT INTO public.medico VALUES (25, 'Genral', 1, 45646);


--
-- TOC entry 3567 (class 0 OID 98590)
-- Dependencies: 234
-- Data for Name: notificacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.notificacion VALUES (26, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788', '2023-05-19 21:33:48.607691', NULL, 25, 8, false);
INSERT INTO public.notificacion VALUES (27, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788', '2023-05-19 21:36:29.730157', NULL, 25, 5, false);
INSERT INTO public.notificacion VALUES (28, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788158 Lng:-63.190764', '2023-05-19 21:38:41.459224', NULL, 24, 26, false);
INSERT INTO public.notificacion VALUES (29, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788158 Lng:-63.190764', '2023-05-19 21:38:42.780864', NULL, 15, 26, false);
INSERT INTO public.notificacion VALUES (30, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788158 Lng:-63.190764', '2023-05-19 21:38:44.087998', NULL, 35, 26, false);
INSERT INTO public.notificacion VALUES (31, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788158 Lng:-63.190764', '2023-05-19 21:38:45.526609', NULL, 28, 26, false);
INSERT INTO public.notificacion VALUES (32, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788158 Lng:-63.190764', '2023-05-19 21:38:46.813217', NULL, 33, 26, false);
INSERT INTO public.notificacion VALUES (33, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788158 Lng:-63.190764', '2023-05-19 21:38:48.080089', NULL, 37, 26, false);
INSERT INTO public.notificacion VALUES (34, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788158 Lng:-63.190764', '2023-05-19 21:38:49.350288', NULL, 34, 26, false);
INSERT INTO public.notificacion VALUES (35, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788158 Lng:-63.190764', '2023-05-19 21:38:50.590714', NULL, 23, 26, false);
INSERT INTO public.notificacion VALUES (36, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788158 Lng:-63.190764', '2023-05-19 21:38:51.881032', NULL, 38, 26, false);
INSERT INTO public.notificacion VALUES (37, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788158 Lng:-63.190764', '2023-05-19 21:40:02.066679', NULL, 10, 15, false);
INSERT INTO public.notificacion VALUES (38, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788216 Lng:-63.1906774', '2023-05-19 21:40:34.181872', NULL, 25, 26, false);
INSERT INTO public.notificacion VALUES (39, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788264 Lng:-63.1906732', '2023-05-19 21:41:55.345338', NULL, 25, 26, false);
INSERT INTO public.notificacion VALUES (40, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788228 Lng:-63.1906577', '2023-05-19 21:42:35.608954', NULL, 25, 26, false);
INSERT INTO public.notificacion VALUES (41, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788639 Lng:-63.1906562', '2023-05-19 21:44:16.735558', NULL, 11, 26, false);
INSERT INTO public.notificacion VALUES (3, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:5717778 y Lat:-17.7971515 Lng:-63.1921377', '2023-04-18 03:58:56.817615', NULL, 15, 4, false);
INSERT INTO public.notificacion VALUES (4, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:5717778 y Lat:-17.7971515 Lng:-63.1921377', '2023-04-18 03:59:30.42593', NULL, 15, 4, false);
INSERT INTO public.notificacion VALUES (5, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8974114 y Lat:-17.7971515 Lng:-63.1921377', '2023-04-18 04:17:32.568502', NULL, 15, 4, false);
INSERT INTO public.notificacion VALUES (6, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255 y Lat:-17.7971515 Lng:-63.1921377', '2023-04-18 04:20:24.207607', NULL, 15, 2, false);
INSERT INTO public.notificacion VALUES (42, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788639 Lng:-63.1906562', '2023-05-19 21:44:18.08064', NULL, 10, 26, false);
INSERT INTO public.notificacion VALUES (43, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788', '2023-05-19 21:48:04.919908', NULL, 18, 5, false);
INSERT INTO public.notificacion VALUES (7, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8767155 con coordenadas Lat:-17.8822567 Lng:-63.0916549', '2023-05-03 16:06:57.839452', NULL, 16, 2, false);
INSERT INTO public.notificacion VALUES (44, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788', '2023-05-19 21:48:04.948454', NULL, 36, 5, false);
INSERT INTO public.notificacion VALUES (2, 'Seguro Scz te informa', 'Emergencia stamos dirigiendo pacientes con ci:5717778 y Lat:-17.7971515 Lng:-63.1921377', '2023-04-17 00:01:54.221568', NULL, 15, 4, false);
INSERT INTO public.notificacion VALUES (45, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788', '2023-05-19 21:48:04.974442', NULL, 39, 5, false);
INSERT INTO public.notificacion VALUES (8, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7790383 Lng:-63.1908283', '2023-05-09 20:16:04.838224', NULL, 16, 26, false);
INSERT INTO public.notificacion VALUES (9, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7790009 Lng:-63.1908168', '2023-05-09 20:17:01.839211', NULL, 24, 26, false);
INSERT INTO public.notificacion VALUES (10, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7790009 Lng:-63.1908168', '2023-05-09 20:17:03.277828', NULL, 15, 26, false);
INSERT INTO public.notificacion VALUES (11, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7790009 Lng:-63.1908168', '2023-05-09 20:17:04.613167', NULL, 23, 26, false);
INSERT INTO public.notificacion VALUES (12, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7789517 Lng:-63.190802', '2023-05-09 20:17:28.059473', NULL, 24, 26, false);
INSERT INTO public.notificacion VALUES (13, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7789517 Lng:-63.190802', '2023-05-09 20:17:29.710436', NULL, 15, 26, false);
INSERT INTO public.notificacion VALUES (14, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7789517 Lng:-63.190802', '2023-05-09 20:17:31.063997', NULL, 23, 26, false);
INSERT INTO public.notificacion VALUES (15, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7789393 Lng:-63.1907845', '2023-05-09 20:18:09.309591', NULL, 24, 26, false);
INSERT INTO public.notificacion VALUES (16, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7789393 Lng:-63.1907845', '2023-05-09 20:18:10.713271', NULL, 15, 26, false);
INSERT INTO public.notificacion VALUES (17, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7789393 Lng:-63.1907845', '2023-05-09 20:18:12.049892', NULL, 23, 26, false);
INSERT INTO public.notificacion VALUES (18, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7789022 Lng:-63.1907421', '2023-05-09 20:20:40.395027', NULL, 11, 26, false);
INSERT INTO public.notificacion VALUES (19, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7789022 Lng:-63.1907421', '2023-05-09 20:20:41.767342', NULL, 10, 26, false);
INSERT INTO public.notificacion VALUES (20, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788', '2023-05-16 21:17:27.618432', NULL, 24, 3, false);
INSERT INTO public.notificacion VALUES (21, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788', '2023-05-16 21:19:40.286585', NULL, 16, 3, false);
INSERT INTO public.notificacion VALUES (22, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788595 Lng:-63.1907488', '2023-05-16 21:25:04.95906', NULL, 24, 26, false);
INSERT INTO public.notificacion VALUES (23, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788595 Lng:-63.1907488', '2023-05-16 21:25:06.259803', NULL, 15, 26, false);
INSERT INTO public.notificacion VALUES (24, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788595 Lng:-63.1907488', '2023-05-16 21:25:07.639823', NULL, 23, 26, false);
INSERT INTO public.notificacion VALUES (25, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788595 Lng:-63.1907488', '2023-05-16 21:29:46.995701', NULL, 10, 24, false);
INSERT INTO public.notificacion VALUES (46, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:33:11.498563', NULL, 15, 5, false);
INSERT INTO public.notificacion VALUES (47, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:33:11.514565', NULL, 37, 5, false);
INSERT INTO public.notificacion VALUES (48, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:33:11.554597', NULL, 33, 5, false);
INSERT INTO public.notificacion VALUES (49, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:33:11.558564', NULL, 34, 5, false);
INSERT INTO public.notificacion VALUES (50, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:33:11.587417', NULL, 28, 5, false);
INSERT INTO public.notificacion VALUES (51, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:33:11.597541', NULL, 35, 5, false);
INSERT INTO public.notificacion VALUES (52, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:37:09.778321', NULL, 17, 5, false);
INSERT INTO public.notificacion VALUES (53, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:39:31.159535', NULL, 24, 5, false);
INSERT INTO public.notificacion VALUES (54, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:42:08.933343', NULL, 16, 5, false);
INSERT INTO public.notificacion VALUES (55, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:49:25.430811', NULL, 39, 5, false);
INSERT INTO public.notificacion VALUES (56, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:49:25.451254', NULL, 18, 5, false);
INSERT INTO public.notificacion VALUES (57, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:49:25.468536', NULL, 36, 5, false);
INSERT INTO public.notificacion VALUES (58, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:51:23.716965', NULL, 23, 5, false);
INSERT INTO public.notificacion VALUES (59, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:51:23.717388', NULL, 38, 5, false);
INSERT INTO public.notificacion VALUES (60, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 04:53:56.954565', NULL, 25, 5, false);
INSERT INTO public.notificacion VALUES (61, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-05-31 05:01:30.855285', NULL, 17, 5, false);
INSERT INTO public.notificacion VALUES (62, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788597 Lng:-63.1906908', '2023-06-01 20:13:17.41556', NULL, 15, 26, false);
INSERT INTO public.notificacion VALUES (63, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788597 Lng:-63.1906908', '2023-06-01 20:13:18.775155', NULL, 35, 26, false);
INSERT INTO public.notificacion VALUES (64, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788597 Lng:-63.1906908', '2023-06-01 20:13:20.312663', NULL, 28, 26, false);
INSERT INTO public.notificacion VALUES (65, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788597 Lng:-63.1906908', '2023-06-01 20:13:22.003636', NULL, 33, 26, false);
INSERT INTO public.notificacion VALUES (66, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788597 Lng:-63.1906908', '2023-06-01 20:13:24.285227', NULL, 37, 26, false);
INSERT INTO public.notificacion VALUES (67, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788597 Lng:-63.1906908', '2023-06-01 20:13:25.572387', NULL, 34, 26, false);
INSERT INTO public.notificacion VALUES (68, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788597 Lng:-63.1906908', '2023-06-01 20:13:26.944068', NULL, 23, 26, false);
INSERT INTO public.notificacion VALUES (69, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788597 Lng:-63.1906908', '2023-06-01 20:13:28.418627', NULL, 38, 26, false);
INSERT INTO public.notificacion VALUES (70, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7788597 Lng:-63.1906908', '2023-06-01 20:13:29.914759', NULL, 24, 26, false);
INSERT INTO public.notificacion VALUES (71, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7786572 Lng:-63.1906918', '2023-06-01 20:22:59.4774', NULL, 15, 26, false);
INSERT INTO public.notificacion VALUES (72, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7786572 Lng:-63.1906918', '2023-06-01 20:23:00.97724', NULL, 35, 26, false);
INSERT INTO public.notificacion VALUES (73, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7786572 Lng:-63.1906918', '2023-06-01 20:23:02.253727', NULL, 28, 26, false);
INSERT INTO public.notificacion VALUES (74, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7786572 Lng:-63.1906918', '2023-06-01 20:23:03.649856', NULL, 33, 26, false);
INSERT INTO public.notificacion VALUES (75, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7786572 Lng:-63.1906918', '2023-06-01 20:23:05.130876', NULL, 37, 26, false);
INSERT INTO public.notificacion VALUES (76, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.7786572 Lng:-63.1906918', '2023-06-01 20:23:06.557633', NULL, 34, 26, false);
INSERT INTO public.notificacion VALUES (77, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-06-02 01:44:08.469206', NULL, 34, 5, false);
INSERT INTO public.notificacion VALUES (78, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-06-02 01:44:08.630584', NULL, 37, 5, false);
INSERT INTO public.notificacion VALUES (79, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-06-02 01:44:08.879504', NULL, 35, 5, false);
INSERT INTO public.notificacion VALUES (80, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-06-02 01:44:09.386978', NULL, 33, 5, false);
INSERT INTO public.notificacion VALUES (81, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-06-02 01:44:09.784205', NULL, 15, 5, false);
INSERT INTO public.notificacion VALUES (82, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-06-02 01:44:09.804813', NULL, 28, 5, false);
INSERT INTO public.notificacion VALUES (83, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.6943968 Lng:-63.159132', '2023-06-02 01:48:58.706849', NULL, 15, 26, false);
INSERT INTO public.notificacion VALUES (84, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.6943968 Lng:-63.159132', '2023-06-02 01:49:00.063409', NULL, 35, 26, false);
INSERT INTO public.notificacion VALUES (85, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.6943968 Lng:-63.159132', '2023-06-02 01:49:01.510626', NULL, 28, 26, false);
INSERT INTO public.notificacion VALUES (86, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.6943968 Lng:-63.159132', '2023-06-02 01:49:02.924351', NULL, 33, 26, false);
INSERT INTO public.notificacion VALUES (87, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.6943968 Lng:-63.159132', '2023-06-02 01:49:04.307763', NULL, 37, 26, false);
INSERT INTO public.notificacion VALUES (88, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.6943968 Lng:-63.159132', '2023-06-02 01:49:05.730593', NULL, 34, 26, false);
INSERT INTO public.notificacion VALUES (89, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.6943968 Lng:-63.159132', '2023-06-02 01:49:07.167818', NULL, 17, 26, false);
INSERT INTO public.notificacion VALUES (90, 'Seguro Scz te informa', 'Emergencia estamos dirigiendo pacientes con ci:8987788 con coordenadas Lat:-17.6943968 Lng:-63.159132', '2023-06-02 01:49:09.03662', NULL, 24, 26, false);
INSERT INTO public.notificacion VALUES (91, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-06-07 13:36:04.340935', NULL, 15, 5, false);
INSERT INTO public.notificacion VALUES (92, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-06-07 13:36:04.613856', NULL, 28, 5, false);
INSERT INTO public.notificacion VALUES (93, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-06-07 13:36:04.630995', NULL, 33, 5, false);
INSERT INTO public.notificacion VALUES (94, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-06-07 13:36:04.65091', NULL, 37, 5, false);
INSERT INTO public.notificacion VALUES (95, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-06-07 13:36:04.661461', NULL, 35, 5, false);
INSERT INTO public.notificacion VALUES (96, 'Seguro Scz te informa', 'Estamos dirigiendo pacientes con ci:8931255', '2023-06-07 13:36:04.701371', NULL, 34, 5, false);


--
-- TOC entry 3569 (class 0 OID 98598)
-- Dependencies: 236
-- Data for Name: operacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.operacion VALUES (5, 'Vesícula', '2016-03-10', 'extirpación', 1);
INSERT INTO public.operacion VALUES (18, 'Húmero', '2019-05-01', 'quebradura de hñumero, tiene placa y clavos', 1);
INSERT INTO public.operacion VALUES (1, 'Colecistectomía', '2023-03-10', 'Es la extirpación quirúrgica de la vesícula biliar. Se realiza para tratar los cálculos biliares y otras afecciones de la vesícula biliar', 3);
INSERT INTO public.operacion VALUES (2, 'Apéndicectomía', '2023-03-15', 'Es la extirpación del apéndice. Se realiza para tratar la apendicitis aguda, una inflamación del apéndice.', 3);
INSERT INTO public.operacion VALUES (3, 'Herniorrafia', '2020-03-15', 'Es la reparación quirúrgica de una hernia. Se realiza para devolver el contenido de la hernia a su posición normal y reforzar el área afectada.', 4);
INSERT INTO public.operacion VALUES (4, 'Artroplastia', '2023-03-15', 'Es la sustitución de una articulación dañada por una prótesis artificial. Se realiza en casos de osteoartritis, artritis reumatoide u otras afecciones que afectan a las articulaciones.', 4);
INSERT INTO public.operacion VALUES (6, 'Cesárea', '2023-04-15', 'Es una operación quirúrgica que se realiza para extraer al feto del útero. Se realiza en casos de parto difícil o peligroso.', 2);
INSERT INTO public.operacion VALUES (7, 'Tiroidectomía', '2023-01-15', ' Es la extirpación quirúrgica de la glándula tiroides. Se realiza para tratar el cáncer de tiroides, nódulos tiroideos o hipertiroidismo.', 6);
INSERT INTO public.operacion VALUES (8, 'Laminectomía', '2023-03-20', ' Es la extirpación quirúrgica de una o más vértebras de la columna vertebral. Se realiza para tratar la estenosis espinal o una hernia de disco.', 6);
INSERT INTO public.operacion VALUES (9, 'Amigdalectomía', '2018-03-15', 'Es la extirpación quirúrgica de las amígdalas. Se realiza para tratar la amigdalitis recurrente o la apnea del sueño.', 7);
INSERT INTO public.operacion VALUES (10, 'Cirujia abdomen', '2002-02-02', 'Impacto vehicular', 5);
INSERT INTO public.operacion VALUES (11, 'cabeza', '1995-06-30', 'delicada', 9);
INSERT INTO public.operacion VALUES (16, 'vejiga', '1998-06-14', '2 sessiones', 9);


--
-- TOC entry 3571 (class 0 OID 98604)
-- Dependencies: 238
-- Data for Name: paciente; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.paciente VALUES (10, 'B+', 'No', 1.25, 60.00, 24);
INSERT INTO public.paciente VALUES (12, 'O+', 'No', 1.78, 81.00, 818419);
INSERT INTO public.paciente VALUES (13, 'O+', 'Si', 1.80, 100.00, 4583724);
INSERT INTO public.paciente VALUES (14, 'A+', 'Si', 1.25, 55.00, 55566);
INSERT INTO public.paciente VALUES (16, 'A+', 'No', 2.22, 22.00, 34323423);
INSERT INTO public.paciente VALUES (17, 'A+', 'No', 1.59, 45.00, 32133);
INSERT INTO public.paciente VALUES (18, 'A+', 'No', 1.23, 55.00, 21323);
INSERT INTO public.paciente VALUES (19, 'B+', 'No', 1.89, 99.00, 312321);
INSERT INTO public.paciente VALUES (20, 'A+', 'Si', 1.55, 56.00, 33333);
INSERT INTO public.paciente VALUES (3, 'O+', 'No', 1.47, 34.00, 5717778);
INSERT INTO public.paciente VALUES (7, 'O+', 'No', 1.55, 21.00, 8931225);
INSERT INTO public.paciente VALUES (8, 'OR+', 'No', 1.75, 90.00, 8987788);
INSERT INTO public.paciente VALUES (4, 'O+', 'Si', 1.60, 54.00, 8955875);
INSERT INTO public.paciente VALUES (5, 'O+', 'Si', 1.80, 65.00, 8955874);
INSERT INTO public.paciente VALUES (6, 'O+', 'Si', 1.96, 76.00, 8974114);
INSERT INTO public.paciente VALUES (9, 'B+', 'Si', 1.75, 50.30, 6965789);
INSERT INTO public.paciente VALUES (11, 'A+', 'No', 47.00, 47.00, 2365);
INSERT INTO public.paciente VALUES (21, 'A+', 'Si', 412.00, 2.00, 432);
INSERT INTO public.paciente VALUES (22, 'O-', 'No', 1.25, 58.69, 5424);
INSERT INTO public.paciente VALUES (23, 'A+', 'Si', 1.31, 55.00, 342432);
INSERT INTO public.paciente VALUES (24, 'A+', 'No', 1.92, 98.00, 321);
INSERT INTO public.paciente VALUES (25, 'A+', 'No', 1.80, 66.00, 65487);
INSERT INTO public.paciente VALUES (26, 'Rh-', 'Si', 1.22, 56.00, 225);
INSERT INTO public.paciente VALUES (27, 'O+', 'Si', 1.65, 85.00, 444444);
INSERT INTO public.paciente VALUES (15, 'A+', 'Si', 1.79, 81.89, 2322);
INSERT INTO public.paciente VALUES (2, 'A+', 'Si', 1.98, 98.50, 8767155);
INSERT INTO public.paciente VALUES (1, 'O+', 'Si', 1.50, 48.00, 8931255);


--
-- TOC entry 3573 (class 0 OID 98608)
-- Dependencies: 240
-- Data for Name: paramedico; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.paramedico VALUES (1, 'Trauma', 1, 8931228);
INSERT INTO public.paramedico VALUES (2, 'Cardiologia', 1, 8931229);
INSERT INTO public.paramedico VALUES (3, 'Emergencias medicas', 2, 8931230);
INSERT INTO public.paramedico VALUES (4, 'Pediatria', 2, 8931231);
INSERT INTO public.paramedico VALUES (5, 'Geriatria', 1, 8931232);
INSERT INTO public.paramedico VALUES (6, 'Salud mental', 2, 8931255);


--
-- TOC entry 3575 (class 0 OID 98612)
-- Dependencies: 242
-- Data for Name: persona; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.persona VALUES (8155654, 'Jesus', 'Hernandez', '1995-05-03', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1682664878/photo/20230428_025435_N84ur.png', NULL, 'b/ 4 de octubre', 'm', 's');
INSERT INTO public.persona VALUES (312321, 'Yenifer', 'Castro Marquez', '2000-02-22', NULL, NULL, 'ddaas', 'm', 'c');
INSERT INTO public.persona VALUES (8974114, 'Joel', 'Perez Ibarra', '1909-03-23', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1684905208/photo/20230524_011326_WJBsj.png', '20230524_011326_WJBsj.png', 'b/magisterio', 'm', 'v');
INSERT INTO public.persona VALUES (8931228, 'Jaime', 'Rios Silva', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', NULL, NULL, 'm', 'c');
INSERT INTO public.persona VALUES (8931229, 'Javier', 'Cardena Rojas', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', NULL, NULL, 'm', 's');
INSERT INTO public.persona VALUES (8931230, 'Fernando Luis', 'Espinoza Sosa', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', NULL, NULL, 'm', 's');
INSERT INTO public.persona VALUES (8931231, 'Yenny', 'Valde Cruz', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', NULL, NULL, 'f', 's');
INSERT INTO public.persona VALUES (8931232, 'Yessica', 'Figueroa Padilla', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', NULL, NULL, 'f', 's');
INSERT INTO public.persona VALUES (8931233, 'Naty', 'Leon Fuente', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', NULL, NULL, 'f', 's');
INSERT INTO public.persona VALUES (8931235, 'Lenny', 'Cortez Lara', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', NULL, NULL, 'f', 'c');
INSERT INTO public.persona VALUES (8931236, 'Romel', 'Lira Luna', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', NULL, NULL, 'm', 'c');
INSERT INTO public.persona VALUES (8931237, 'Hector', 'Martinez Lopez', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', NULL, NULL, 'm', 'c');
INSERT INTO public.persona VALUES (8931238, 'Ismael', 'Jimenez Diaz', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', NULL, NULL, 'm', 'c');
INSERT INTO public.persona VALUES (8931239, 'Andres', 'Diaz Reyes', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', NULL, NULL, 'm', 'c');
INSERT INTO public.persona VALUES (8931240, 'Armando', 'Perez Flores', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', NULL, NULL, 'm', 's');
INSERT INTO public.persona VALUES (8931241, 'Felipe', 'Garcia Rodriguez', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', NULL, NULL, 'm', 's');
INSERT INTO public.persona VALUES (8931242, 'Susan', 'Perez Herrera', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', NULL, NULL, 'f', 's');
INSERT INTO public.persona VALUES (8767155, 'Lius', 'Escamilla Galvan', '1998-03-23', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1684905086/photo/20230524_011124_kCO7r.png', '20230524_011124_kCO7r.png', NULL, 'm', 'c');
INSERT INTO public.persona VALUES (8955875, 'Lurdez', 'James Gil', '2003-03-23', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1684905114/photo/20230524_011152_DecHq.png', '20230524_011152_DecHq.png', 'b/villaalegre', 'f', 's');
INSERT INTO public.persona VALUES (8955874, 'Grecia', 'Mendoza', '2012-03-23', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1684905134/photo/20230524_011212_w1fBO.png', '20230524_011212_w1fBO.png', 'b/boo', 'f', 's');
INSERT INTO public.persona VALUES (8931225, 'Javier', 'Espino Guerra', '1989-03-23', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1681419280/perfil/1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', '1012974_894947463851852_577701170769649666_n_fk8nhy.jpg', 'b/claveles', 'm', 's');
INSERT INTO public.persona VALUES (8931234, 'Maria', 'Fuentes Rojas', '1998-05-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1682664878/photo/20230428_025435_N84ur.png', '20230428_025435_N84ur.png', NULL, 'f', 'c');
INSERT INTO public.persona VALUES (8989871, 'German Jose', 'Guerra', '1991-02-02', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1682664878/photo/20230428_025435_N84ur.png', NULL, NULL, 'm', 'c');
INSERT INTO public.persona VALUES (8989872, 'Andrez', 'Hernan G.', '1882-02-04', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1682664878/photo/20230428_025435_N84ur.png', NULL, NULL, 'm', 's');
INSERT INTO public.persona VALUES (8989873, 'Luciana', 'Luz', '1967-01-02', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1682664878/photo/20230428_025435_N84ur.png', NULL, NULL, 'f', 'c');
INSERT INTO public.persona VALUES (8987788, 'Juan Pablo', 'Gutierrez', '1985-01-01', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1682664878/photo/20230428_025435_N84ur.png', NULL, 'av/ banzer', 'm', 's');
INSERT INTO public.persona VALUES (8155645, 'Walter', 'Mamani Janco', '1992-07-26', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1682664878/photo/20230428_025435_N84ur.png', NULL, 'b/ Cenotrop', 'm', 's');
INSERT INTO public.persona VALUES (8155673, 'ss', 'ss', '1923-04-03', NULL, NULL, 'sd', 'm', 's');
INSERT INTO public.persona VALUES (665878, 'pablo', 'roman', '1999-12-12', NULL, NULL, 'b/ds', 'm', 's');
INSERT INTO public.persona VALUES (6658732, 'pablo', 'roman', '1999-12-12', NULL, NULL, 'b/ds', 'm', 's');
INSERT INTO public.persona VALUES (798888, 'wa', 'wa', '2023-05-24', NULL, NULL, 'ww', 'h', 's');
INSERT INTO public.persona VALUES (8765400, 'as', 'as', '2023-05-05', NULL, NULL, 'as', 'nb', 'v');
INSERT INTO public.persona VALUES (8931441, 'saa', 'saa', '2023-05-20', NULL, NULL, 'sa', 'm', 'c');
INSERT INTO public.persona VALUES (8765456, '1232', '12', '2023-05-25', NULL, NULL, '232', 'm', 's');
INSERT INTO public.persona VALUES (12325222, 'qwe', 'qwe', '2023-05-25', NULL, NULL, 'ewq', 'm', 'v');
INSERT INTO public.persona VALUES (8931448, 'ds', 'dsa', '2023-05-20', NULL, NULL, 'dsa', 'h', 's');
INSERT INTO public.persona VALUES (323, 'dasd', 'asdsa', '2023-05-17', NULL, NULL, 'asdsa', 'h', 's');
INSERT INTO public.persona VALUES (65478, 'german', 'paco', '2023-05-20', NULL, NULL, 'bdd/ddd', 'bi', 's');
INSERT INTO public.persona VALUES (665822, 'pablo', 'roman', '1999-12-12', NULL, NULL, 'b/ds', 'm', 's');
INSERT INTO public.persona VALUES (1234433, 'dsad', 'dasdd', '2023-05-25', NULL, NULL, 'dsa', 'h', 's');
INSERT INTO public.persona VALUES (8765401, 'fo', 'fo', '2023-05-18', NULL, NULL, 'sa', 'bi', 's');
INSERT INTO public.persona VALUES (8765000, 'qdq', 'dw', '2023-05-18', NULL, NULL, 'qqqq', 'ag', 's');
INSERT INTO public.persona VALUES (432432, 'wqwe', 'ewqe', '2023-05-19', NULL, NULL, '312321', 'h', 's');
INSERT INTO public.persona VALUES (1234, 'josue', 'andia', '2023-05-11', NULL, NULL, 'b/dfsd', 'nb', 's');
INSERT INTO public.persona VALUES (696544, 'donald', 'xavier', '2023-05-19', NULL, NULL, '312321', 'h', 's');
INSERT INTO public.persona VALUES (22, 'julian', 'alvares', '2023-05-04', NULL, NULL, 'd', 'nb', 'v');
INSERT INTO public.persona VALUES (23, 'donald', 'xavier', '2023-05-19', NULL, NULL, '312321', 'nb', 'v');
INSERT INTO public.persona VALUES (55566, 'luis', 'fernades', '3300-11-11', NULL, NULL, 'dsa', 'h', 's');
INSERT INTO public.persona VALUES (33333, 'demo', 'pri', '2036-01-22', NULL, NULL, 'dsa', 'h', 's');
INSERT INTO public.persona VALUES (5717778, 'Gael', 'Rojas', '1933-03-23', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1684904832/photo/20230524_010700_uUTmh.png', '20230524_010700_uUTmh.png', 'b/elfuerte', 'm', 'c');
INSERT INTO public.persona VALUES (4583724, 'Juan Pablo', 'Gutierrez', '1979-06-07', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685371458/photo/20230529_144418_F5Ok0.webp', '20230529_144418_F5Ok0.webp', 'Calle X #10', 'h', 's');
INSERT INTO public.persona VALUES (8931255, 'Pedro', 'Gonzales Escobar', '1992-08-23', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685103212/photo/20230526_121332_nmEVZ.jpg', '20230526_121332_nmEVZ.jpg', 'B/ Olivos', 'h', 'c');
INSERT INTO public.persona VALUES (24, 'Marcelo', 'xavier', '1985-05-05', NULL, NULL, 'N/N', 'nb', 'v');
INSERT INTO public.persona VALUES (21323, 'Santiago ', 'Romero', '2214-03-22', NULL, NULL, 'asdsad', 'h', 's');
INSERT INTO public.persona VALUES (32133, 'Junior ', 'Escobar Ali', '2223-03-22', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685158260/photo/20230526_233058_TqMMZ.jpg', '20230526_233058_TqMMZ.jpg', 'sdas', 'h', 's');
INSERT INTO public.persona VALUES (2365, 'albvaro', 'soliz', '2023-05-10', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685174581/photo/20230527_040258_vRKbD.png', '20230527_040258_vRKbD.png', 'b lotes', 'h', 'c');
INSERT INTO public.persona VALUES (3332, 'das', 'das', NULL, 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685674650/perfil/perfiluserdefault_ax7rd1.png', NULL, 'dsa', 'h', 'c');
INSERT INTO public.persona VALUES (5424, 'jose jose', 'salvatierrra', '1996-12-12', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685674650/perfil/perfiluserdefault_ax7rd1.png', NULL, 'los olivos', 'h', 's');
INSERT INTO public.persona VALUES (342432, 'Javier', 'duran', '2023-04-03', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685674650/perfil/perfiluserdefault_ax7rd1.png', NULL, 'calle esapña', 'h', 's');
INSERT INTO public.persona VALUES (321, 'Mihael', 'Hurtado', '2018-06-06', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685674650/perfil/perfiluserdefault_ax7rd1.png', NULL, 'calle 7', 'h', 'd');
INSERT INTO public.persona VALUES (65487, 'noe', 'nuñes', '2023-06-13', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685674650/perfil/perfiluserdefault_ax7rd1.png', NULL, 'dasd', 'h', 's');
INSERT INTO public.persona VALUES (444444, 'Juan Carlos', 'Ramos', '2014-06-12', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685674650/perfil/perfiluserdefault_ax7rd1.png', NULL, 'Calle Las Garzas # 145', 'h', 's');
INSERT INTO public.persona VALUES (2322, 'Juan Pablo', 'Jimenez', '1975-11-12', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1686030910/photo/20230606_015506_X9qW8.png', '20230606_015506_X9qW8.png', 'Los Valles', 'h', 's');
INSERT INTO public.persona VALUES (34323423, 'Pedro Xavier', 'Cuellar Jacinto', '2000-11-11', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1686176987/photo/20230607_182940_6fJb5.png', '20230607_182940_6fJb5.png', 'Barrio El Fuerte Nro.55', 'h', 'v');
INSERT INTO public.persona VALUES (432, 'Julia', 'Escobar', '2023-06-06', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685674650/perfil/perfiluserdefault_ax7rd1.png', NULL, 'dsacsd', 'm', 's');
INSERT INTO public.persona VALUES (225, 'Maguie', 'Duran Gonzales', '1995-06-06', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685674650/perfil/perfiluserdefault_ax7rd1.png', NULL, 'barrio El Fuerte', 'm', 's');
INSERT INTO public.persona VALUES (818419, 'Pelayo', 'Tapia Lopez', '1999-06-23', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1684905261/photo/20230524_011419_HQ0be.png', '20230524_011419_HQ0be.png', 'Octavo Anillo', 'h', 's');
INSERT INTO public.persona VALUES (6965789, 'Jacobo', 'Benegaz Cacerez', '1972-05-19', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1684905577/photo/20230524_011935_4guiz.png', '20230524_011935_4guiz.png', '5to anillo radial 10', 'h', 'd');
INSERT INTO public.persona VALUES (365255, 'Julian', 'Alvarez', '1999-12-22', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685674650/perfil/perfiluserdefault_ax7rd1.png', NULL, 'Calle Sucre', 'h', 's');
INSERT INTO public.persona VALUES (365254, 'Felipe', 'Alvarez', '1985-12-20', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685674650/perfil/perfiluserdefault_ax7rd1.png', NULL, 'Calle uno', 'h', 's');
INSERT INTO public.persona VALUES (55699, 'Tamara', 'Gallardo', '1978-05-22', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685674650/perfil/perfiluserdefault_ax7rd1.png', NULL, 'Calle 2 ', 'm', 'c');
INSERT INTO public.persona VALUES (45646, 'Maria Juana', 'Bellido', '2002-02-02', 'https://res.cloudinary.com/dci37dfd7/image/upload/v1685674650/perfil/perfiluserdefault_ax7rd1.png', NULL, 'calle lujan', 'm', 's');


--
-- TOC entry 3576 (class 0 OID 98618)
-- Dependencies: 243
-- Data for Name: phone; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.phone VALUES (2, '7985642', 'tio', 8767155);
INSERT INTO public.phone VALUES (5, '8788955', 'personal', 5717778);
INSERT INTO public.phone VALUES (8, '78418755', 'Vecino', 5717778);
INSERT INTO public.phone VALUES (21, '798855', 'mama', 8955874);
INSERT INTO public.phone VALUES (22, '454455', 'yerno', 8955875);
INSERT INTO public.phone VALUES (23, '7964522', 'Primo', 8767155);
INSERT INTO public.phone VALUES (24, '6464948', 'Vecino', 8767155);
INSERT INTO public.phone VALUES (25, '4789798', 'Papa', 8955874);
INSERT INTO public.phone VALUES (27, '7898822', 'Hermano', 8955875);
INSERT INTO public.phone VALUES (4, '7454551', 'Tia lejana', 5717778);
INSERT INTO public.phone VALUES (29, '468748', 'padre', 32133);
INSERT INTO public.phone VALUES (31, '778899', 'padre', 8974114);
INSERT INTO public.phone VALUES (33, '723213', 'personal', 65487);
INSERT INTO public.phone VALUES (30, '31322', 'Vecino', 2365);
INSERT INTO public.phone VALUES (32, '23322332', 'gato', 6965789);
INSERT INTO public.phone VALUES (7, '79486701', 'Tio', 8987788);
INSERT INTO public.phone VALUES (16, '76328028', 'hermano', 8931255);
INSERT INTO public.phone VALUES (35, '7216655', 'Padre', 6965789);


--
-- TOC entry 3578 (class 0 OID 98622)
-- Dependencies: 245
-- Data for Name: rol; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.rol VALUES (1, 'admin');
INSERT INTO public.rol VALUES (2, 'medico');
INSERT INTO public.rol VALUES (3, 'chofer');
INSERT INTO public.rol VALUES (4, 'paramedico');
INSERT INTO public.rol VALUES (5, 'paciente');


--
-- TOC entry 3580 (class 0 OID 98626)
-- Dependencies: 247
-- Data for Name: siniestro; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.siniestro VALUES (1, 'opcion de fe', '1999-12-12 08:24:31', 14.12000000, 2.25000000, 5);


--
-- TOC entry 3582 (class 0 OID 98630)
-- Dependencies: 249
-- Data for Name: tokens; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tokens VALUES (131, 7, 'fU1V3LQmTaykhb_tSTvEJT:APA91bE0IIfPw9VHkwiooZmUKh9MFiVhbMpqbwFLp5LMghKHa2FHYOy6C95QEV7RQqz_Y-cWrjCGpxCeE9BGzDxfOjK2XlWbe2PtGyHwT9YK1TbfrayCxDsJP2k6dQQEbbAmc49nbPzi', '2023-05-09 20:42:08.816325', NULL);
INSERT INTO public.tokens VALUES (132, 11, 'cxtKFPq4QZ6Luoy0ZYrSds:APA91bFUCkKD1J1663NfnGOgRammzrgV6_wgeBzwvbcnjJj_xK5Cc_74vLRUCGJV96TNvRy3HmI-AOmx7DDkwoLyABuWTkP0-5pnS5QbSWSpjBLeFQHw2427mCnixtXUvxR664ov3pyx', '2023-05-09 20:44:30.903684', NULL);
INSERT INTO public.tokens VALUES (135, 19, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-09 20:46:00.4996', NULL);
INSERT INTO public.tokens VALUES (139, 7, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-14 22:31:21.584485', NULL);
INSERT INTO public.tokens VALUES (142, 18, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-16 17:00:49.240227', NULL);
INSERT INTO public.tokens VALUES (144, 10, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-16 17:42:43.604016', NULL);
INSERT INTO public.tokens VALUES (146, 14, 'eLVuCBjxTUeQDJbMfDp7sX:APA91bFLOkk_zdDlL3erIE_9-oMs-VSActcRj-Ma3Y0KYKu89dLnccJfGY5C6YnCRuINo4HJWfyDQh8Y3jGz7etL7X65UUNUzbp-_1Y17oqMlXTarKHUZTlOayiWNhAAGwxIvAIB-FNB', '2023-05-16 19:45:48.36349', NULL);
INSERT INTO public.tokens VALUES (147, 14, 'eLVuCBjxTUeQDJbMfDp7sX:APA91bFLOkk_zdDlL3erIE_9-oMs-VSActcRj-Ma3Y0KYKu89dLnccJfGY5C6YnCRuINo4HJWfyDQh8Y3jGz7etL7X65UUNUzbp-_1Y17oqMlXTarKHUZTlOayiWNhAAGwxIvAIB-FNB', '2023-05-16 19:45:50.009467', NULL);
INSERT INTO public.tokens VALUES (148, 14, 'eLVuCBjxTUeQDJbMfDp7sX:APA91bFLOkk_zdDlL3erIE_9-oMs-VSActcRj-Ma3Y0KYKu89dLnccJfGY5C6YnCRuINo4HJWfyDQh8Y3jGz7etL7X65UUNUzbp-_1Y17oqMlXTarKHUZTlOayiWNhAAGwxIvAIB-FNB', '2023-05-16 19:45:50.010613', NULL);
INSERT INTO public.tokens VALUES (149, 14, 'duCShTlKSKGtdczkN73ar6:APA91bFDuoFldaKjDM7PtTmkypnzDPaeWmWC5xkChs51hT4J4c8iZgrcaRk_GMEWQb2Lx669CKbqeq__ivePqLqZECp35gyCGLR8UdDZV-dx6hbYXoZU4vDK5dd-xYvgy3Thjbqn95Vn', '2023-05-16 20:49:22.17017', NULL);
INSERT INTO public.tokens VALUES (110, 16, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-09 17:25:15.264129', NULL);
INSERT INTO public.tokens VALUES (111, 26, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-09 17:28:40.643367', NULL);
INSERT INTO public.tokens VALUES (112, 6, 'fU1V3LQmTaykhb_tSTvEJT:APA91bE0IIfPw9VHkwiooZmUKh9MFiVhbMpqbwFLp5LMghKHa2FHYOy6C95QEV7RQqz_Y-cWrjCGpxCeE9BGzDxfOjK2XlWbe2PtGyHwT9YK1TbfrayCxDsJP2k6dQQEbbAmc49nbPzi', '2023-05-09 19:13:03.82384', NULL);
INSERT INTO public.tokens VALUES (113, 6, 'fU1V3LQmTaykhb_tSTvEJT:APA91bE0IIfPw9VHkwiooZmUKh9MFiVhbMpqbwFLp5LMghKHa2FHYOy6C95QEV7RQqz_Y-cWrjCGpxCeE9BGzDxfOjK2XlWbe2PtGyHwT9YK1TbfrayCxDsJP2k6dQQEbbAmc49nbPzi', '2023-05-09 19:13:06.685713', NULL);
INSERT INTO public.tokens VALUES (150, 27, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-16 21:04:51.905287', NULL);
INSERT INTO public.tokens VALUES (249, 5, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-31 19:20:10.737962', NULL);
INSERT INTO public.tokens VALUES (250, 16, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-31 20:35:03.411273', NULL);
INSERT INTO public.tokens VALUES (114, 15, 'fU1V3LQmTaykhb_tSTvEJT:APA91bE0IIfPw9VHkwiooZmUKh9MFiVhbMpqbwFLp5LMghKHa2FHYOy6C95QEV7RQqz_Y-cWrjCGpxCeE9BGzDxfOjK2XlWbe2PtGyHwT9YK1TbfrayCxDsJP2k6dQQEbbAmc49nbPzi', '2023-05-09 20:14:51.022109', NULL);
INSERT INTO public.tokens VALUES (115, 15, 'fU1V3LQmTaykhb_tSTvEJT:APA91bE0IIfPw9VHkwiooZmUKh9MFiVhbMpqbwFLp5LMghKHa2FHYOy6C95QEV7RQqz_Y-cWrjCGpxCeE9BGzDxfOjK2XlWbe2PtGyHwT9YK1TbfrayCxDsJP2k6dQQEbbAmc49nbPzi', '2023-05-09 20:14:51.285766', NULL);
INSERT INTO public.tokens VALUES (266, 14, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-06-01 20:53:53.151762', NULL);
INSERT INTO public.tokens VALUES (268, 18, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-06-01 20:56:59.197928', NULL);
INSERT INTO public.tokens VALUES (269, 10, 'c_mOlelNRF-hyLxEsgYOOa:APA91bHPzk2mPrw9tyGTRyptZJHBsDKqty3eXIB0mqiDJuxjW0Aob2UAGP5110_cF4hXNHkmS25oWoszFC-EiRfniNBqOtbZioQUjYNTQM8tlCoRGxEIfOdNV-vzJP1-FLNsODXEc5zL', '2023-06-02 01:39:00.153029', NULL);
INSERT INTO public.tokens VALUES (119, 11, 'fU1V3LQmTaykhb_tSTvEJT:APA91bE0IIfPw9VHkwiooZmUKh9MFiVhbMpqbwFLp5LMghKHa2FHYOy6C95QEV7RQqz_Y-cWrjCGpxCeE9BGzDxfOjK2XlWbe2PtGyHwT9YK1TbfrayCxDsJP2k6dQQEbbAmc49nbPzi', '2023-05-09 20:21:18.416666', NULL);
INSERT INTO public.tokens VALUES (271, 5, 'cV-UZZ6hSr-LpI8DMZzIJj:APA91bERnKr933L9wpoKiKGTH-86ZqR-iT_KZ66YRdHz12DAB78sOlzre4MgrRrXYv1Ld3LmvFfpHScVRcqfVjsk4hBkhviXt8mp418b_6ErePZN9cnfTW4U2xZ83gdPAk0GBPgFr-a0', '2023-06-02 01:40:10.428572', NULL);
INSERT INTO public.tokens VALUES (120, 15, 'cxtKFPq4QZ6Luoy0ZYrSds:APA91bFUCkKD1J1663NfnGOgRammzrgV6_wgeBzwvbcnjJj_xK5Cc_74vLRUCGJV96TNvRy3HmI-AOmx7DDkwoLyABuWTkP0-5pnS5QbSWSpjBLeFQHw2427mCnixtXUvxR664ov3pyx', '2023-05-09 20:21:48.93877', NULL);
INSERT INTO public.tokens VALUES (275, 15, 'fqoVRuacSmqfolQBzImAIi:APA91bEoeytGWk2dV0lZoBarhOgW83FvUGjwoc_lNwjn06vUpTTVhN_u5GaRRsYJfEKXiD8g80zG1xe-tWtMYmEoVqFBYeAR3U5uQpvPAzDlcyYt1L4aPHrU0dkQvDv2hyAzUDFT2c3O', '2023-06-02 01:46:31.789137', NULL);
INSERT INTO public.tokens VALUES (280, 10, 'fqoVRuacSmqfolQBzImAIi:APA91bEoeytGWk2dV0lZoBarhOgW83FvUGjwoc_lNwjn06vUpTTVhN_u5GaRRsYJfEKXiD8g80zG1xe-tWtMYmEoVqFBYeAR3U5uQpvPAzDlcyYt1L4aPHrU0dkQvDv2hyAzUDFT2c3O', '2023-06-07 13:26:47.009058', NULL);
INSERT INTO public.tokens VALUES (282, 5, 'cV-UZZ6hSr-LpI8DMZzIJj:APA91bERnKr933L9wpoKiKGTH-86ZqR-iT_KZ66YRdHz12DAB78sOlzre4MgrRrXYv1Ld3LmvFfpHScVRcqfVjsk4hBkhviXt8mp418b_6ErePZN9cnfTW4U2xZ83gdPAk0GBPgFr-a0', '2023-06-07 13:34:17.42826', NULL);
INSERT INTO public.tokens VALUES (283, 26, 'cV-UZZ6hSr-LpI8DMZzIJj:APA91bERnKr933L9wpoKiKGTH-86ZqR-iT_KZ66YRdHz12DAB78sOlzre4MgrRrXYv1Ld3LmvFfpHScVRcqfVjsk4hBkhviXt8mp418b_6ErePZN9cnfTW4U2xZ83gdPAk0GBPgFr-a0', '2023-06-08 13:43:31.449446', NULL);
INSERT INTO public.tokens VALUES (284, 5, 'cV-UZZ6hSr-LpI8DMZzIJj:APA91bERnKr933L9wpoKiKGTH-86ZqR-iT_KZ66YRdHz12DAB78sOlzre4MgrRrXYv1Ld3LmvFfpHScVRcqfVjsk4hBkhviXt8mp418b_6ErePZN9cnfTW4U2xZ83gdPAk0GBPgFr-a0', '2023-06-08 16:09:45.343739', NULL);
INSERT INTO public.tokens VALUES (285, 26, 'fw2FFsxJTc-JobifrA8BaA:APA91bFsw_Tr96I_BjLz_P6zscw45lQvFJlh6-UM_UtjJ0DKt5YyNHdA2LbFeBmcwG7ouLWem5bCHhIBazCLepdZQqC0xeCSQ4TQfCF66u-LjtLamdFMqlRU8kPlftG8H2jb52w_ChI1', '2023-06-09 14:02:09.800864', NULL);
INSERT INTO public.tokens VALUES (153, 3, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-16 21:09:08.470579', NULL);
INSERT INTO public.tokens VALUES (158, 17, 'duCShTlKSKGtdczkN73ar6:APA91bFDuoFldaKjDM7PtTmkypnzDPaeWmWC5xkChs51hT4J4c8iZgrcaRk_GMEWQb2Lx669CKbqeq__ivePqLqZECp35gyCGLR8UdDZV-dx6hbYXoZU4vDK5dd-xYvgy3Thjbqn95Vn', '2023-05-16 21:17:12.786739', NULL);
INSERT INTO public.tokens VALUES (160, 26, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-16 21:23:03.371897', NULL);
INSERT INTO public.tokens VALUES (162, 24, 'duCShTlKSKGtdczkN73ar6:APA91bFDuoFldaKjDM7PtTmkypnzDPaeWmWC5xkChs51hT4J4c8iZgrcaRk_GMEWQb2Lx669CKbqeq__ivePqLqZECp35gyCGLR8UdDZV-dx6hbYXoZU4vDK5dd-xYvgy3Thjbqn95Vn', '2023-05-16 21:25:39.35734', NULL);
INSERT INTO public.tokens VALUES (163, 10, 'eLVuCBjxTUeQDJbMfDp7sX:APA91bFLOkk_zdDlL3erIE_9-oMs-VSActcRj-Ma3Y0KYKu89dLnccJfGY5C6YnCRuINo4HJWfyDQh8Y3jGz7etL7X65UUNUzbp-_1Y17oqMlXTarKHUZTlOayiWNhAAGwxIvAIB-FNB', '2023-05-16 21:29:37.825599', NULL);
INSERT INTO public.tokens VALUES (164, 10, 'eLVuCBjxTUeQDJbMfDp7sX:APA91bFLOkk_zdDlL3erIE_9-oMs-VSActcRj-Ma3Y0KYKu89dLnccJfGY5C6YnCRuINo4HJWfyDQh8Y3jGz7etL7X65UUNUzbp-_1Y17oqMlXTarKHUZTlOayiWNhAAGwxIvAIB-FNB', '2023-05-16 21:29:39.698993', NULL);
INSERT INTO public.tokens VALUES (165, 18, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-19 17:41:28.361119', NULL);
INSERT INTO public.tokens VALUES (168, 15, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-19 17:43:19.261654', NULL);
INSERT INTO public.tokens VALUES (169, 14, 'dKGyrkG7QImEoaJK2cW2Ke:APA91bGj5N15lT9kcMtURJ4GrVSg-QFUOqchLRqQYF6PYPfqyvdWH06eds-BaWcT6q9C2uSgiTpU_opWQb48Nf2yhNreCs9QSUanEavJRmlLciMM_QbEfZWr28IKBhprbNEjIgaTWauw', '2023-05-19 19:36:45.173457', NULL);
INSERT INTO public.tokens VALUES (173, 5, 'dKGyrkG7QImEoaJK2cW2Ke:APA91bGj5N15lT9kcMtURJ4GrVSg-QFUOqchLRqQYF6PYPfqyvdWH06eds-BaWcT6q9C2uSgiTpU_opWQb48Nf2yhNreCs9QSUanEavJRmlLciMM_QbEfZWr28IKBhprbNEjIgaTWauw', '2023-05-19 21:20:43.640333', NULL);
INSERT INTO public.tokens VALUES (247, 18, 'eWnS2DywSEqvGBw9uco-hU:APA91bF3MwEc6yzgeiopo-O_q9jCKMdP6qxi75dBaETz3aRSdf2fQHAGr8mQH9u0pCn3ZzPXoFknifuS_aC88Z1OBXd-BWs9CEvf123cX3uPpV3i-_36e69K1LzuWrOr43s7k6dcYNPa', '2023-05-31 05:17:59.231747', NULL);
INSERT INTO public.tokens VALUES (251, 5, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-31 21:26:33.805226', NULL);
INSERT INTO public.tokens VALUES (253, 26, 'cV-UZZ6hSr-LpI8DMZzIJj:APA91bERnKr933L9wpoKiKGTH-86ZqR-iT_KZ66YRdHz12DAB78sOlzre4MgrRrXYv1Ld3LmvFfpHScVRcqfVjsk4hBkhviXt8mp418b_6ErePZN9cnfTW4U2xZ83gdPAk0GBPgFr-a0', '2023-06-01 20:10:33.866638', NULL);
INSERT INTO public.tokens VALUES (186, 10, 'duCShTlKSKGtdczkN73ar6:APA91bFDuoFldaKjDM7PtTmkypnzDPaeWmWC5xkChs51hT4J4c8iZgrcaRk_GMEWQb2Lx669CKbqeq__ivePqLqZECp35gyCGLR8UdDZV-dx6hbYXoZU4vDK5dd-xYvgy3Thjbqn95Vn', '2023-05-19 21:39:55.831397', NULL);
INSERT INTO public.tokens VALUES (265, 26, 'cV-UZZ6hSr-LpI8DMZzIJj:APA91bERnKr933L9wpoKiKGTH-86ZqR-iT_KZ66YRdHz12DAB78sOlzre4MgrRrXYv1Ld3LmvFfpHScVRcqfVjsk4hBkhviXt8mp418b_6ErePZN9cnfTW4U2xZ83gdPAk0GBPgFr-a0', '2023-06-01 20:53:43.814242', NULL);
INSERT INTO public.tokens VALUES (192, 15, 'duCShTlKSKGtdczkN73ar6:APA91bFDuoFldaKjDM7PtTmkypnzDPaeWmWC5xkChs51hT4J4c8iZgrcaRk_GMEWQb2Lx669CKbqeq__ivePqLqZECp35gyCGLR8UdDZV-dx6hbYXoZU4vDK5dd-xYvgy3Thjbqn95Vn', '2023-05-19 21:47:53.791615', NULL);
INSERT INTO public.tokens VALUES (272, 15, 'fqoVRuacSmqfolQBzImAIi:APA91bEoeytGWk2dV0lZoBarhOgW83FvUGjwoc_lNwjn06vUpTTVhN_u5GaRRsYJfEKXiD8g80zG1xe-tWtMYmEoVqFBYeAR3U5uQpvPAzDlcyYt1L4aPHrU0dkQvDv2hyAzUDFT2c3O', '2023-06-02 01:41:02.669747', NULL);
INSERT INTO public.tokens VALUES (274, 15, 'fqoVRuacSmqfolQBzImAIi:APA91bEoeytGWk2dV0lZoBarhOgW83FvUGjwoc_lNwjn06vUpTTVhN_u5GaRRsYJfEKXiD8g80zG1xe-tWtMYmEoVqFBYeAR3U5uQpvPAzDlcyYt1L4aPHrU0dkQvDv2hyAzUDFT2c3O', '2023-06-02 01:41:02.858511', NULL);
INSERT INTO public.tokens VALUES (196, 14, 'cksz9X8cQYKXrGnd6sUdqP:APA91bETu3kP5dYucPA-j8ZBpqJJaTpx6vC2C3lxfe6cdGaSQfCwDXcWrWrjk7R_fB7ZO73qmGLa6e1rtXGknDmShFIEFPF35qbe9CwrocdSXhZF_qwoNREh8syoQCioQyVyvOT5MMSt', '2023-05-22 02:20:56.158356', NULL);
INSERT INTO public.tokens VALUES (279, 26, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-06-05 20:21:56.761972', NULL);
INSERT INTO public.tokens VALUES (281, 15, 'c_mOlelNRF-hyLxEsgYOOa:APA91bHPzk2mPrw9tyGTRyptZJHBsDKqty3eXIB0mqiDJuxjW0Aob2UAGP5110_cF4hXNHkmS25oWoszFC-EiRfniNBqOtbZioQUjYNTQM8tlCoRGxEIfOdNV-vzJP1-FLNsODXEc5zL', '2023-06-07 13:28:25.93988', NULL);
INSERT INTO public.tokens VALUES (286, 26, 'fw2FFsxJTc-JobifrA8BaA:APA91bFsw_Tr96I_BjLz_P6zscw45lQvFJlh6-UM_UtjJ0DKt5YyNHdA2LbFeBmcwG7ouLWem5bCHhIBazCLepdZQqC0xeCSQ4TQfCF66u-LjtLamdFMqlRU8kPlftG8H2jb52w_ChI1', '2023-06-09 14:02:09.949394', NULL);
INSERT INTO public.tokens VALUES (200, 3, 'cksz9X8cQYKXrGnd6sUdqP:APA91bETu3kP5dYucPA-j8ZBpqJJaTpx6vC2C3lxfe6cdGaSQfCwDXcWrWrjk7R_fB7ZO73qmGLa6e1rtXGknDmShFIEFPF35qbe9CwrocdSXhZF_qwoNREh8syoQCioQyVyvOT5MMSt', '2023-05-26 12:18:21.021327', NULL);
INSERT INTO public.tokens VALUES (201, 18, 'cksz9X8cQYKXrGnd6sUdqP:APA91bETu3kP5dYucPA-j8ZBpqJJaTpx6vC2C3lxfe6cdGaSQfCwDXcWrWrjk7R_fB7ZO73qmGLa6e1rtXGknDmShFIEFPF35qbe9CwrocdSXhZF_qwoNREh8syoQCioQyVyvOT5MMSt', '2023-05-26 15:21:53.706624', NULL);
INSERT INTO public.tokens VALUES (202, 16, 'dgJqe6nzT5WLsUjEHSWq6J:APA91bH5ZLlr6lEQOqnXv-hPjaetRMVYZZr5GocSf4bgFrQuZpfx1O47RHo8E8abzs7NdlpVmwhaEuGVfFQ8Yz1vRB-1VpkUB6a-NsQb0iqSiBkuz4649UgKaScdy5BAjpWeIGDggsEK', '2023-05-27 02:13:49.714767', NULL);
INSERT INTO public.tokens VALUES (204, 10, 'd8J-MrnQSdKoN16DPS_E3Z:APA91bFYeOd8-uJwrGIfJ0bRxruE5wLP2bk6qC6NBRaeOO3pDU4KAakpQQnBFSOvacYzOjgj8bUw6gYrAy_w6G7N118WllPfAjMw5hs7jrxZcN8Jvy8oFznWfJB2VlScBQbUkRRuRjvF', '2023-05-29 19:20:27.197195', NULL);
INSERT INTO public.tokens VALUES (205, 3, 'd8J-MrnQSdKoN16DPS_E3Z:APA91bFYeOd8-uJwrGIfJ0bRxruE5wLP2bk6qC6NBRaeOO3pDU4KAakpQQnBFSOvacYzOjgj8bUw6gYrAy_w6G7N118WllPfAjMw5hs7jrxZcN8Jvy8oFznWfJB2VlScBQbUkRRuRjvF', '2023-05-29 19:25:39.126736', NULL);
INSERT INTO public.tokens VALUES (206, 10, 'd8J-MrnQSdKoN16DPS_E3Z:APA91bFYeOd8-uJwrGIfJ0bRxruE5wLP2bk6qC6NBRaeOO3pDU4KAakpQQnBFSOvacYzOjgj8bUw6gYrAy_w6G7N118WllPfAjMw5hs7jrxZcN8Jvy8oFznWfJB2VlScBQbUkRRuRjvF', '2023-05-30 21:36:44.03511', NULL);
INSERT INTO public.tokens VALUES (209, 18, 'eWnS2DywSEqvGBw9uco-hU:APA91bF3MwEc6yzgeiopo-O_q9jCKMdP6qxi75dBaETz3aRSdf2fQHAGr8mQH9u0pCn3ZzPXoFknifuS_aC88Z1OBXd-BWs9CEvf123cX3uPpV3i-_36e69K1LzuWrOr43s7k6dcYNPa', '2023-05-30 22:11:10.919608', NULL);


--
-- TOC entry 3584 (class 0 OID 98635)
-- Dependencies: 251
-- Data for Name: tratamiento; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3586 (class 0 OID 98641)
-- Dependencies: 253
-- Data for Name: ubicacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.ubicacion VALUES (1, -17.786290, -63.181170, '2023-06-10 03:30:51.297319', 24, 1);
INSERT INTO public.ubicacion VALUES (2, -17.786290, -63.181170, '2023-06-09 23:38:39.813854', 24, 1);
INSERT INTO public.ubicacion VALUES (3, -17.786290, -63.181170, '2023-06-09 23:50:15.080412', 24, 1);
INSERT INTO public.ubicacion VALUES (4, -17.786290, -63.181170, '2023-06-09 23:50:17.84274', 24, 1);
INSERT INTO public.ubicacion VALUES (5, -17.786290, -63.181170, '2023-06-09 23:50:20.700822', 24, 1);
INSERT INTO public.ubicacion VALUES (6, -17.786290, -63.181170, '2023-06-09 23:51:00.770858', 55566, 1);
INSERT INTO public.ubicacion VALUES (7, -17.786290, -63.181170, '2023-06-09 23:51:03.922891', 55566, 1);


--
-- TOC entry 3588 (class 0 OID 98646)
-- Dependencies: 255
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.usuario VALUES (4, 'paramedico', 'pbkdf2:sha256:260000$mLm0TcXA4cFdTvw4$f46d2a2a24d176dec431fd37fd4d38e921acd8fc5a482b7fcb23f4b367d54b31', 'paramedico@gmail.com', 'act', NULL, 5, 8931225);
INSERT INTO public.usuario VALUES (11, 'chofer2', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'verde.natura98@yahoo.com', 'act', NULL, 3, 8931235);
INSERT INTO public.usuario VALUES (15, 'medico4', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'ardiente.corazon_67@gmail.com', 'act', NULL, 2, 8931239);
INSERT INTO public.usuario VALUES (6, 'leo', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'asd@gmail.com', 'act', NULL, 4, 8931230);
INSERT INTO public.usuario VALUES (7, 'pablito', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'po@sss.co', 'act', NULL, 4, 8931231);
INSERT INTO public.usuario VALUES (8, 'latino', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'pp@ss.bo', 'act', NULL, 4, 8931232);
INSERT INTO public.usuario VALUES (9, 'luminoso', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'negro.azabache22@icloud.com', 'act', NULL, 5, 8931233);
INSERT INTO public.usuario VALUES (16, 'medico3', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'riosalvaje99@yahoo.com', 'act', NULL, 2, 8931240);
INSERT INTO public.usuario VALUES (35, 'gis32', 'pbkdf2:sha256:260000$JhJ4zvSTZc5EtZWA$0bf14e617ec2fc50d4cf76b49579404a786db403644858289a122dd6cac27acd', 'll1@ll.cc', 'act', NULL, 2, 665822);
INSERT INTO public.usuario VALUES (17, 'medico2', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'montana.azul_12@outlook.com', 'act', NULL, 2, 8931241);
INSERT INTO public.usuario VALUES (18, 'medico1', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'mariposa.magica_8@gmail.com', 'act', NULL, 2, 8931242);
INSERT INTO public.usuario VALUES (23, 'medico5', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'pp@ss.ff', 'act', NULL, 2, 8989871);
INSERT INTO public.usuario VALUES (24, 'medico6', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'kk@hh.oo', 'act', NULL, 2, 8989872);
INSERT INTO public.usuario VALUES (25, 'medico7', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'uu@rr.yy', 'act', NULL, 2, 8989873);
INSERT INTO public.usuario VALUES (26, 'paciente10', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'jp@gg.cc', 'act', NULL, 5, 8987788);
INSERT INTO public.usuario VALUES (27, 'chofer12', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'ch1@mm.cc', 'act', NULL, 3, 8155645);
INSERT INTO public.usuario VALUES (28, 'chofer13', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'ch2@pp.xx', 'act', NULL, 3, 8155654);
INSERT INTO public.usuario VALUES (3, 'paramedico1', 'pbkdf2:sha256:260000$nWmrRNiwYPbQ9hSX$e4c79c9d45aa669d9f2c07fc0fc27c5a2b0a4d3809e66f563d4547236b463dfe', 'perro@gg.co', 'act', 'assaddfffa', 4, 8155673);
INSERT INTO public.usuario VALUES (33, 'gis', 'pbkdf2:sha256:260000$G0rXXhCdM7DkZe4Z$be156a3189b3710e91f1fdaadafbaea183f2b57cc9040cc6208f594d012f5553', 'll@ll.cc', 'act', NULL, 3, 665878);
INSERT INTO public.usuario VALUES (36, 'sass22', 'pbkdf2:sha256:260000$8ff0Nt28BCZ6csYi$97aef305f6ea305ce6159d3884845c2228c388826535843f792ab5c68e200964', 'as12@sd.ss', 'act', NULL, 2, 8765401);
INSERT INTO public.usuario VALUES (37, 'wq', 'pbkdf2:sha256:260000$gA8kPYzrkERMOwPF$3312f5040fb77499675e1ef38c830bb59fdcdd23b33acff55967f469c10826bc', 'qew@dsa.sd', 'act', NULL, 2, 8765000);
INSERT INTO public.usuario VALUES (38, 'das233', 'pbkdf2:sha256:260000$jXfEHLcGTKh5rLcb$6cc4f136daa283dc07312eaf93e0b77bab47e7ab4d5e96003b086693ddda55ce', 'ewqe@ee.432', 'act', NULL, 2, 432432);
INSERT INTO public.usuario VALUES (39, 'numero1', 'pbkdf2:sha256:260000$oORftzxyvsYGmzOS$9f356a83df573c3732f74e3a0fb2e0c87e81ed46ab8f56e48367941bafceee76', 'dd@gg.xx', 'act', NULL, 2, 1234);
INSERT INTO public.usuario VALUES (19, 'lunaplateada', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'luna.plateada_45@yahoo.com', 'act', NULL, 4, 8931255);
INSERT INTO public.usuario VALUES (20, 'mendez', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'men@hh.cc', 'act', NULL, 5, 8955874);
INSERT INTO public.usuario VALUES (1, 'luzu', 'pbkdf2:sha256:260000$ArDqsLTo6IZ2XDIA$7e8c9b37686d1e749ce2cd2009c1094a8dfea8c2430c5762063e313c21d4a2ef', 'admin@segruro.com', 'act', NULL, 5, 5717778);
INSERT INTO public.usuario VALUES (2, 'maicol58', 'pbkdf2:sha256:260000$dBTu46S6fCQlxU8o$337ca0c4dfe538a8b97f3a4225448c7585bc0b7e9a9642b7d7e90e2c32a7997a', 'maik@hotmail.com', 'act', NULL, 5, 8767155);
INSERT INTO public.usuario VALUES (12, 'manchester', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'azulmarino123@gmail.com', 'act', NULL, 3, 8931236);
INSERT INTO public.usuario VALUES (13, 'fuegorojo', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'rojo.fuego56@hotmail.com', 'act', NULL, 3, 8931237);
INSERT INTO public.usuario VALUES (21, 'lopez', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'lol@hh.cc', 'act', NULL, 5, 8955875);
INSERT INTO public.usuario VALUES (34, 'gis2', 'pbkdf2:sha256:260000$8kit4xkYw9NbZwwm$1d4d6b6534790ee4b4d239ab7652c3686a6ead34fdfd9867fdefa0a800e30fc4', 'll@ll.cc', 'act', NULL, 3, 6658732);
INSERT INTO public.usuario VALUES (14, 'Admin', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'Admin@gmail.com', 'act', NULL, 1, 8931228);
INSERT INTO public.usuario VALUES (40, 'kai22', 'pbkdf2:sha256:260000$TvF73bb9lkn3SvJt$e6589d42ad77952861cbc438cb84e9c4cbae8a5d7303e899475d615ad7926cc3', 'ewqe@ee.432', 'act', NULL, 5, 6965789);
INSERT INTO public.usuario VALUES (5, 'paramedico2', 'pbkdf2:sha256:260000$MFqPgpejMxkMYAXP$82e1b2183fa4aec65f63df53aad7dd937c8b8e1ba2b2da117ea81998f70b6555', 'sd@ss.com', 'act', NULL, 4, 8931229);
INSERT INTO public.usuario VALUES (22, 'paciente1', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'sos@hh.cc', 'act', NULL, 5, 8974114);
INSERT INTO public.usuario VALUES (10, 'chofer1', 'pbkdf2:sha256:260000$WEHClMe9iQ04Tm24$b18cfd474ea5c8a168bf1b4dcf40c6c65d88defcc0784587d796a0797c3e8267', 'amarillo.sol77@outlook.com', 'act', NULL, 3, 8931234);
INSERT INTO public.usuario VALUES (41, 'sudo54', 'pbkdf2:sha256:260000$Y2DuXB0pQB58JxHM$8e72d68a2afbd63b9d56e8adbd7fe38ded54cac4c9a7d93361a0294ebeb860b6', 'ds@dd.cc', 'act', NULL, 5, 24);
INSERT INTO public.usuario VALUES (42, 'al55', 'pbkdf2:sha256:260000$CTE5uClwPanA8RZy$50e97d82a8636eea4183baee66cab8ae797ecf7fdd1faab32df4ef32a592bb12', 'oo@pp.gg', 'act', NULL, 5, 2365);
INSERT INTO public.usuario VALUES (43, 'Pelay', 'pbkdf2:sha256:260000$H2DdP19LQeKSn2bw$75a3cb46158092fc8e772bdb5ad7ea4e77e6f2f24f37badc7388019f88360b91', 'pelay@gmail.com', 'act', NULL, 5, 818419);
INSERT INTO public.usuario VALUES (44, 'xjpx', 'pbkdf2:sha256:260000$WFGJ6PDUB6dHQLcr$8841b88395da31e9431cbd161a3d270dae33dd12307acc6c555cdf6d0299e8cf', 'juanpablo@hotmail.com', 'act', NULL, 5, 4583724);
INSERT INTO public.usuario VALUES (45, 'lf45', 'pbkdf2:sha256:260000$D3RImCg0n86XTefF$f9fe7fe8a0c6a0d64dadced303b513206d81b54113628a32eb70c59d85109d7c', 'ds@dd.cd', 'act', NULL, 5, 55566);
INSERT INTO public.usuario VALUES (46, '34344', 'pbkdf2:sha256:260000$8hXmpOvyyZmypduJ$6c3cf0293ccaa3bb14cd8635c8d40e1fd5009674ff0e1fe963bbc67a352c5493', 'dfsa@dsad.ds', 'act', NULL, 5, 2322);
INSERT INTO public.usuario VALUES (47, '32', 'pbkdf2:sha256:260000$QRLkrdx5cEkEoGNh$dd7ed2e4539297d26c113c046d83b1a6c75437b5eb4ace171b332e15d987e978', 'dfsa@dsad11.ds', 'act', NULL, 5, 34323423);
INSERT INTO public.usuario VALUES (48, 'dasdas', 'pbkdf2:sha256:260000$pGKLaG5I8JixzMXw$16ff8559ccd8f357e06412d8d7ff93717bbcf04a91f2351629901a162aa21e43', 'dfsa@dsad112.ds', 'act', NULL, 5, 32133);
INSERT INTO public.usuario VALUES (49, 'de323', 'pbkdf2:sha256:260000$VHTZlK0YyeScVQ5y$af51d03b7c167071fdf4c9b33ac42694020e08aec327ee7b87c8261251c60ae2', 'dfsa@dsad111.ds', 'act', NULL, 5, 21323);
INSERT INTO public.usuario VALUES (50, 'dasdas123234', 'pbkdf2:sha256:260000$UohIJdoD5w3wIb35$76146349d363083477645398dd4389b61c9c1c3aa3fee19780ca34bd1ab94458', 'dfsa@dsad11.ds', 'act', NULL, 5, 312321);
INSERT INTO public.usuario VALUES (51, 'dsa', 'pbkdf2:sha256:260000$CttLRcXXM8kW5DRr$41a01cf83b5b522aaa621200f027266b28a2f63255f3862c7f90cfae2466cd75', 'dfsa@dsad112.ds', 'act', NULL, 5, 33333);
INSERT INTO public.usuario VALUES (52, 'dsadsa', 'pbkdf2:sha256:260000$MHHAOXv5AqmyiaTZ$0c037a23e54cf850450e559763f610c1da0714550cfefc01056c68f6131f5916', '123', 'act', NULL, 5, 432);
INSERT INTO public.usuario VALUES (53, 'maxhg', 'pbkdf2:sha256:260000$JJPRb4U8euv4UDy5$6081329218e5ff904ed68086896bae09d6f9540b409ad752c5ebe5244271e26e', '123', 'act', NULL, 5, 5424);
INSERT INTO public.usuario VALUES (54, 'durann', 'pbkdf2:sha256:260000$gV8fBEl3JVQ4HclE$0b3a6d1375e028ac78a15478225eca3f9e7aa714234729023744332257337c94', '123', 'act', NULL, 5, 342432);
INSERT INTO public.usuario VALUES (57, 'ww', 'pbkdf2:sha256:260000$DCZnDK50A0avJVQL$a0c5d93f756eca7b7da665e4f71f649364a0f56e7d62434e16b3f92fc4880c65', 'ss@ss.ssss', 'act', NULL, 5, 225);
INSERT INTO public.usuario VALUES (56, 'noeon', 'pbkdf2:sha256:260000$LrkdXokNYLtA1N3q$e87c778bc27d2e279949af4f42e2f8d6fc7c3aefab330a2f596e4e9845933834', 'noe@gm.com', 'act', NULL, 5, 65487);
INSERT INTO public.usuario VALUES (58, 'jcr', 'pbkdf2:sha256:260000$CCM3QwY1gSoRHTQE$14d122930668f46dfef5e7fa1e0293ee9d8161b704d1e2b3ee582f24c61fb702', 'juancarlosramos@gmail.com', 'act', NULL, 5, 444444);
INSERT INTO public.usuario VALUES (59, 'falvare', 'pbkdf2:sha256:260000$fhctVJ1AFHfGLNT8$54771e5893ae399145d4341783bc946e1e755a115f9b215c6ad4df995a666384', 'fa@gmail.com', 'act', NULL, 2, 365254);
INSERT INTO public.usuario VALUES (60, 'tmara', 'pbkdf2:sha256:260000$Gwgb6noGVXoianYk$882fad89ddbaa49930221c3a3987d2daea02deacaed57c10f9344a17ad3de524', 'tam@gmail.com', 'act', NULL, 2, 55699);
INSERT INTO public.usuario VALUES (61, 'belli', 'pbkdf2:sha256:260000$xRY2ch1nCDggkpuO$ffe4f781513ede111c0d06bba6c55fe346db586156a6e82fe5fa06793960eded', 'b@hotmail.com', 'act', NULL, 2, 45646);


--
-- TOC entry 3590 (class 0 OID 98653)
-- Dependencies: 257
-- Data for Name: vacuna; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.vacuna VALUES (1, 'Covid', 3, 1);
INSERT INTO public.vacuna VALUES (2, 'AHN1', 1, 1);
INSERT INTO public.vacuna VALUES (3, 'Janssen', 1, 2);
INSERT INTO public.vacuna VALUES (4, 'Covanix', 2, 2);
INSERT INTO public.vacuna VALUES (5, 'Sinovac', 2, 3);
INSERT INTO public.vacuna VALUES (6, 'Moderna', 2, 3);
INSERT INTO public.vacuna VALUES (7, 'J&J', 1, 4);
INSERT INTO public.vacuna VALUES (8, 'Bhtac', 2, 4);
INSERT INTO public.vacuna VALUES (9, 'Covid', 4, 5);
INSERT INTO public.vacuna VALUES (10, 'pfres', 4, 5);
INSERT INTO public.vacuna VALUES (11, 'Impacto', 1, 7);
INSERT INTO public.vacuna VALUES (12, 'Personal', 12, 9);
INSERT INTO public.vacuna VALUES (13, 'Colab', 11, 9);


--
-- TOC entry 3620 (class 0 OID 0)
-- Dependencies: 215
-- Name: alergia_idale_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.alergia_idale_seq', 40, true);


--
-- TOC entry 3621 (class 0 OID 0)
-- Dependencies: 217
-- Name: ambulancia_idam_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ambulancia_idam_seq', 11, true);


--
-- TOC entry 3622 (class 0 OID 0)
-- Dependencies: 219
-- Name: chofer_idch_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.chofer_idch_seq', 6, true);


--
-- TOC entry 3623 (class 0 OID 0)
-- Dependencies: 221
-- Name: dispositivo_iddis_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dispositivo_iddis_seq', 3, true);


--
-- TOC entry 3624 (class 0 OID 0)
-- Dependencies: 223
-- Name: documento_historial_clinico_iddoc_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.documento_historial_clinico_iddoc_seq', 25, true);


--
-- TOC entry 3625 (class 0 OID 0)
-- Dependencies: 225
-- Name: emergencia_idem_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.emergencia_idem_seq', 80, true);


--
-- TOC entry 3626 (class 0 OID 0)
-- Dependencies: 227
-- Name: enfermedad_idenf_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.enfermedad_idenf_seq', 43, true);


--
-- TOC entry 3627 (class 0 OID 0)
-- Dependencies: 229
-- Name: hospital_idh_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hospital_idh_seq', 7, true);


--
-- TOC entry 3628 (class 0 OID 0)
-- Dependencies: 231
-- Name: medicamento_idme_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.medicamento_idme_seq', 27, true);


--
-- TOC entry 3629 (class 0 OID 0)
-- Dependencies: 233
-- Name: medico_idmed_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.medico_idmed_seq', 25, true);


--
-- TOC entry 3630 (class 0 OID 0)
-- Dependencies: 235
-- Name: notificacion_idnoti_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.notificacion_idnoti_seq', 96, true);


--
-- TOC entry 3631 (class 0 OID 0)
-- Dependencies: 237
-- Name: operacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.operacion_id_seq', 18, true);


--
-- TOC entry 3632 (class 0 OID 0)
-- Dependencies: 239
-- Name: paciente_idpac_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.paciente_idpac_seq', 27, true);


--
-- TOC entry 3633 (class 0 OID 0)
-- Dependencies: 241
-- Name: paramedico_idpar_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.paramedico_idpar_seq', 6, true);


--
-- TOC entry 3634 (class 0 OID 0)
-- Dependencies: 244
-- Name: phone_idp_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.phone_idp_seq', 35, true);


--
-- TOC entry 3635 (class 0 OID 0)
-- Dependencies: 246
-- Name: rol_idrol_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.rol_idrol_seq', 6, true);


--
-- TOC entry 3636 (class 0 OID 0)
-- Dependencies: 248
-- Name: siniestro_ids_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.siniestro_ids_seq', 1, true);


--
-- TOC entry 3637 (class 0 OID 0)
-- Dependencies: 250
-- Name: tokens_idt_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tokens_idt_seq', 286, true);


--
-- TOC entry 3638 (class 0 OID 0)
-- Dependencies: 252
-- Name: tratamiento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tratamiento_id_seq', 1, false);


--
-- TOC entry 3639 (class 0 OID 0)
-- Dependencies: 254
-- Name: ubicacion_idubi_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ubicacion_idubi_seq', 7, true);


--
-- TOC entry 3640 (class 0 OID 0)
-- Dependencies: 256
-- Name: usuario_idu_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuario_idu_seq', 61, true);


--
-- TOC entry 3641 (class 0 OID 0)
-- Dependencies: 258
-- Name: vacuna_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vacuna_id_seq', 13, true);


--
-- TOC entry 3331 (class 2606 OID 98680)
-- Name: alergia alergia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alergia
    ADD CONSTRAINT alergia_pkey PRIMARY KEY (idale);


--
-- TOC entry 3333 (class 2606 OID 98682)
-- Name: ambulancia ambulancia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ambulancia
    ADD CONSTRAINT ambulancia_pkey PRIMARY KEY (idam);


--
-- TOC entry 3336 (class 2606 OID 98684)
-- Name: chofer chofer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chofer
    ADD CONSTRAINT chofer_pkey PRIMARY KEY (idch);


--
-- TOC entry 3338 (class 2606 OID 98686)
-- Name: dispositivo dispositivo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispositivo
    ADD CONSTRAINT dispositivo_pkey PRIMARY KEY (iddis);


--
-- TOC entry 3340 (class 2606 OID 98688)
-- Name: documento documento_historial_clinico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.documento
    ADD CONSTRAINT documento_historial_clinico_pkey PRIMARY KEY (iddoc);


--
-- TOC entry 3342 (class 2606 OID 98690)
-- Name: emergencia emergencia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emergencia
    ADD CONSTRAINT emergencia_pkey PRIMARY KEY (idem);


--
-- TOC entry 3344 (class 2606 OID 98692)
-- Name: enfermedad enfermedad_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enfermedad
    ADD CONSTRAINT enfermedad_pkey PRIMARY KEY (idenf);


--
-- TOC entry 3346 (class 2606 OID 98694)
-- Name: hospital hospital_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hospital
    ADD CONSTRAINT hospital_pkey PRIMARY KEY (idh);


--
-- TOC entry 3348 (class 2606 OID 98696)
-- Name: medicamento medicamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medicamento
    ADD CONSTRAINT medicamento_pkey PRIMARY KEY (idme);


--
-- TOC entry 3351 (class 2606 OID 98698)
-- Name: medico medico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medico
    ADD CONSTRAINT medico_pkey PRIMARY KEY (idmed);


--
-- TOC entry 3353 (class 2606 OID 98700)
-- Name: notificacion notificacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notificacion
    ADD CONSTRAINT notificacion_pkey PRIMARY KEY (idnoti);


--
-- TOC entry 3355 (class 2606 OID 98702)
-- Name: operacion operacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operacion
    ADD CONSTRAINT operacion_pkey PRIMARY KEY (idop);


--
-- TOC entry 3357 (class 2606 OID 98704)
-- Name: paciente paciente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paciente
    ADD CONSTRAINT paciente_pkey PRIMARY KEY (idpac);


--
-- TOC entry 3359 (class 2606 OID 98706)
-- Name: paramedico paramedico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paramedico
    ADD CONSTRAINT paramedico_pkey PRIMARY KEY (idpar);


--
-- TOC entry 3361 (class 2606 OID 98708)
-- Name: persona persona_pkey1; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.persona
    ADD CONSTRAINT persona_pkey1 PRIMARY KEY (ci);


--
-- TOC entry 3363 (class 2606 OID 98710)
-- Name: phone phone_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone
    ADD CONSTRAINT phone_pkey PRIMARY KEY (idp);


--
-- TOC entry 3365 (class 2606 OID 98712)
-- Name: rol rol_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rol
    ADD CONSTRAINT rol_pkey PRIMARY KEY (idrol);


--
-- TOC entry 3367 (class 2606 OID 98714)
-- Name: siniestro siniestro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.siniestro
    ADD CONSTRAINT siniestro_pkey PRIMARY KEY (ids);


--
-- TOC entry 3369 (class 2606 OID 98716)
-- Name: tokens tokens_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tokens
    ADD CONSTRAINT tokens_pkey PRIMARY KEY (idt);


--
-- TOC entry 3371 (class 2606 OID 98718)
-- Name: tratamiento tratamiento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tratamiento
    ADD CONSTRAINT tratamiento_pkey PRIMARY KEY (idtra);


--
-- TOC entry 3373 (class 2606 OID 98720)
-- Name: ubicacion ubicacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ubicacion
    ADD CONSTRAINT ubicacion_pkey PRIMARY KEY (idubi);


--
-- TOC entry 3376 (class 2606 OID 98722)
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (idu);


--
-- TOC entry 3378 (class 2606 OID 98724)
-- Name: usuario usuario_un; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_un UNIQUE (nameuser);


--
-- TOC entry 3380 (class 2606 OID 98726)
-- Name: vacuna vacuna_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacuna
    ADD CONSTRAINT vacuna_pkey PRIMARY KEY (idvac);


--
-- TOC entry 3334 (class 1259 OID 98727)
-- Name: ambulancia_placa_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ambulancia_placa_idx ON public.ambulancia USING btree (placa);


--
-- TOC entry 3349 (class 1259 OID 98728)
-- Name: medico_ci_persona_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX medico_ci_persona_idx ON public.medico USING btree (ci_persona);


--
-- TOC entry 3374 (class 1259 OID 98729)
-- Name: usuario_ci_persona_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX usuario_ci_persona_idx ON public.usuario USING btree (ci_persona);


--
-- TOC entry 3381 (class 2606 OID 98730)
-- Name: alergia alergia_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alergia
    ADD CONSTRAINT alergia_fk FOREIGN KEY (paciente_id) REFERENCES public.paciente(idpac);


--
-- TOC entry 3382 (class 2606 OID 98735)
-- Name: chofer chofer_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chofer
    ADD CONSTRAINT chofer_fk FOREIGN KEY (ci_persona) REFERENCES public.persona(ci);


--
-- TOC entry 3383 (class 2606 OID 98740)
-- Name: chofer chofer_id_ambulancia_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chofer
    ADD CONSTRAINT chofer_id_ambulancia_fkey FOREIGN KEY (id_ambulancia) REFERENCES public.ambulancia(idam);


--
-- TOC entry 3384 (class 2606 OID 98745)
-- Name: documento documento_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.documento
    ADD CONSTRAINT documento_fk FOREIGN KEY (paciente_id) REFERENCES public.paciente(idpac);


--
-- TOC entry 3385 (class 2606 OID 98750)
-- Name: emergencia emergencia_id_ambulancia_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emergencia
    ADD CONSTRAINT emergencia_id_ambulancia_fkey FOREIGN KEY (id_ambulancia) REFERENCES public.ambulancia(idam);


--
-- TOC entry 3386 (class 2606 OID 98755)
-- Name: emergencia emergencia_id_hospital_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emergencia
    ADD CONSTRAINT emergencia_id_hospital_fkey FOREIGN KEY (id_hospital) REFERENCES public.hospital(idh);


--
-- TOC entry 3387 (class 2606 OID 98760)
-- Name: enfermedad enfermedad2_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enfermedad
    ADD CONSTRAINT enfermedad2_fk FOREIGN KEY (paciente_id) REFERENCES public.paciente(idpac);


--
-- TOC entry 3388 (class 2606 OID 98765)
-- Name: medicamento medicamento_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medicamento
    ADD CONSTRAINT medicamento_fk FOREIGN KEY (paciente_id) REFERENCES public.paciente(idpac);


--
-- TOC entry 3389 (class 2606 OID 98770)
-- Name: medico medico_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medico
    ADD CONSTRAINT medico_fk FOREIGN KEY (ci_persona) REFERENCES public.persona(ci);


--
-- TOC entry 3390 (class 2606 OID 98775)
-- Name: medico medico_hospital_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medico
    ADD CONSTRAINT medico_hospital_id_fkey FOREIGN KEY (hospital_id) REFERENCES public.hospital(idh);


--
-- TOC entry 3391 (class 2606 OID 98780)
-- Name: notificacion notificacion_user_remitente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notificacion
    ADD CONSTRAINT notificacion_user_remitente_fkey FOREIGN KEY (user_remitente) REFERENCES public.usuario(idu);


--
-- TOC entry 3392 (class 2606 OID 98785)
-- Name: operacion operacion_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operacion
    ADD CONSTRAINT operacion_fk FOREIGN KEY (paciente_id) REFERENCES public.paciente(idpac);


--
-- TOC entry 3393 (class 2606 OID 98790)
-- Name: paciente paciente_ci_persona_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paciente
    ADD CONSTRAINT paciente_ci_persona_fkey FOREIGN KEY (ci_persona) REFERENCES public.persona(ci);


--
-- TOC entry 3394 (class 2606 OID 98795)
-- Name: paramedico paramedico_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paramedico
    ADD CONSTRAINT paramedico_fk FOREIGN KEY (ci_persona) REFERENCES public.persona(ci);


--
-- TOC entry 3395 (class 2606 OID 98800)
-- Name: paramedico paramedico_id_ambulancia_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paramedico
    ADD CONSTRAINT paramedico_id_ambulancia_fkey FOREIGN KEY (id_ambulancia) REFERENCES public.ambulancia(idam);


--
-- TOC entry 3396 (class 2606 OID 98805)
-- Name: phone phone_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone
    ADD CONSTRAINT phone_fk FOREIGN KEY (ci_persona) REFERENCES public.persona(ci);


--
-- TOC entry 3397 (class 2606 OID 98810)
-- Name: siniestro siniestro_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.siniestro
    ADD CONSTRAINT siniestro_fk FOREIGN KEY (paciente_id) REFERENCES public.paciente(idpac);


--
-- TOC entry 3398 (class 2606 OID 98815)
-- Name: tokens tokens_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tokens
    ADD CONSTRAINT tokens_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.usuario(idu);


--
-- TOC entry 3399 (class 2606 OID 98820)
-- Name: tratamiento tratamiento_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tratamiento
    ADD CONSTRAINT tratamiento_fk FOREIGN KEY (idenf) REFERENCES public.enfermedad(idenf);


--
-- TOC entry 3400 (class 2606 OID 98825)
-- Name: ubicacion ubicacion_dispositivo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ubicacion
    ADD CONSTRAINT ubicacion_dispositivo_id_fkey FOREIGN KEY (dispositivo_id) REFERENCES public.dispositivo(iddis);


--
-- TOC entry 3401 (class 2606 OID 98830)
-- Name: ubicacion ubicacion_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ubicacion
    ADD CONSTRAINT ubicacion_fk FOREIGN KEY (persona_ci) REFERENCES public.persona(ci);


--
-- TOC entry 3402 (class 2606 OID 98835)
-- Name: usuario usuario2_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario2_fk FOREIGN KEY (ci_persona) REFERENCES public.persona(ci);


--
-- TOC entry 3403 (class 2606 OID 98840)
-- Name: usuario usuario_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_fk FOREIGN KEY (idrol) REFERENCES public.rol(idrol);


--
-- TOC entry 3404 (class 2606 OID 98845)
-- Name: vacuna vacuna_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacuna
    ADD CONSTRAINT vacuna_fk FOREIGN KEY (paciente_id) REFERENCES public.paciente(idpac);


-- Completed on 2023-10-03 21:57:42

--
-- PostgreSQL database dump complete
--

