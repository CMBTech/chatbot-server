--
-- PostgreSQL database dump
--

-- Dumped from database version 10.18 (Ubuntu 10.18-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.18 (Ubuntu 10.18-0ubuntu0.18.04.1)

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
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;


--
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: hmutegeki
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO hmutegeki;

--
-- Name: category; Type: TABLE; Schema: public; Owner: hmutegeki
--

CREATE TABLE public.category (
    id integer NOT NULL,
    name character varying(256),
    menu_value integer NOT NULL
);


ALTER TABLE public.category OWNER TO hmutegeki;

--
-- Name: category_id_seq; Type: SEQUENCE; Schema: public; Owner: hmutegeki
--

CREATE SEQUENCE public.category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_id_seq OWNER TO hmutegeki;

--
-- Name: category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hmutegeki
--

ALTER SEQUENCE public.category_id_seq OWNED BY public.category.id;


--
-- Name: platform; Type: TABLE; Schema: public; Owner: hmutegeki
--

CREATE TABLE public.platform (
    id integer NOT NULL,
    name character varying(256),
    url character varying(256),
    status_date character varying,
    category_id integer NOT NULL,
    status boolean,
    menu_value integer NOT NULL,
    report_id character varying(256) NOT NULL
);


ALTER TABLE public.platform OWNER TO hmutegeki;

--
-- Name: platform_id_seq; Type: SEQUENCE; Schema: public; Owner: hmutegeki
--

CREATE SEQUENCE public.platform_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.platform_id_seq OWNER TO hmutegeki;

--
-- Name: platform_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hmutegeki
--

ALTER SEQUENCE public.platform_id_seq OWNED BY public.platform.id;


--
-- Name: category id; Type: DEFAULT; Schema: public; Owner: hmutegeki
--

ALTER TABLE ONLY public.category ALTER COLUMN id SET DEFAULT nextval('public.category_id_seq'::regclass);


--
-- Name: platform id; Type: DEFAULT; Schema: public; Owner: hmutegeki
--

ALTER TABLE ONLY public.platform ALTER COLUMN id SET DEFAULT nextval('public.platform_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: hmutegeki
--

COPY public.alembic_version (version_num) FROM stdin;
8782e77e72a8
\.


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: hmutegeki
--

COPY public.category (id, name, menu_value) FROM stdin;
1	socials	3
2	vpn	4
3	News sites	5
4	Civil society organizations	6
\.


--
-- Data for Name: platform; Type: TABLE DATA; Schema: public; Owner: hmutegeki
--

COPY public.platform (id, name, url, status_date, category_id, status, menu_value, report_id) FROM stdin;
2	facebook	facebook.com	Saturday 04 September 2021 at 23:40	1	t	2	20210407T180249Z_facebookmessenger_UG_20294_n1_x71fmhkRPLbIJLsA
1	twitter	twitter.com	Saturday 04 September 2021 at 23:40	1	f	1	20210406T103932Z_webconnectivity_UG_36991_n1_B1JhJZjdOT2VihlG
3	Signal	\N	2021-09-08 20:52:28.902832+03	1	\N	8	20210419T022319Z_signal_UG_20294_n1_ch4e8o0EjWpLZOOa
4	Whatsapp	\N	2021-09-08 20:53:25.355956+03	1	\N	9	20210419T022313Z_whatsapp_UG_20294_n1_3vrwtdDoNUeBdxoi
5	Telegram	\N	2021-09-08 20:54:12.154341+03	1	\N	10	20210419T021210Z_webconnectivity_UG_20294_n1_E8PSMpANPdDx42iY
6	New Vision	\N	2021-09-08 20:55:12.064164+03	3	\N	11	20210826T135515Z_webconnectivity_UG_36991_n1_OrNQicHk5Gz1Tdmj
7	Observer	\N	2021-09-08 20:56:38.514104+03	3	\N	12	20210826T111854Z_webconnectivity_UG_36991_n1_AZmY2ue0ocV5QyDU
8	Psiphon	\N	2021-09-08 20:57:53.473949+03	2	\N	13	20210410T123229Z_psiphon_UG_20294_n1_3xFuCS6BSo8YyxU7
9	RiseUp	\N	2021-09-08 20:58:41.753039+03	2	\N	14	20210409T073302Z_riseupvpn_UG_37063_n1_Phxvb00nIrU5BM9D
10	Tor	\N	2021-09-08 20:59:26.128511+03	2	\N	15	20210409T073220Z_tor_UG_37063_n1_bUdasorpuIXMxCPK
11	unwantedwitness.or.ug	\N	2021-09-08 21:02:49.862314+03	4	\N	16	20210831T075442Z_webconnectivity_UG_36991_n1_ooRjQcHfou45JOMz
12	Nilepost	\N	2021-09-08 21:04:00.539836+03	3	\N	17	20210823T053822Z_webconnectivity_UG_36991_n1_WznV2CIZcDFUhWUJ
13	Amnesty	\N	2021-09-08 21:05:53.100167+03	4	\N	18	20210902T060523Z_webconnectivity_UG_36991_n1_MKTAPner0oKaUdTJ
\.


--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hmutegeki
--

SELECT pg_catalog.setval('public.category_id_seq', 4, true);


--
-- Name: platform_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hmutegeki
--

SELECT pg_catalog.setval('public.platform_id_seq', 13, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: hmutegeki
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: category category_pkey; Type: CONSTRAINT; Schema: public; Owner: hmutegeki
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (id);


--
-- Name: platform platform_pkey; Type: CONSTRAINT; Schema: public; Owner: hmutegeki
--

ALTER TABLE ONLY public.platform
    ADD CONSTRAINT platform_pkey PRIMARY KEY (id);


--
-- Name: platform platform_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hmutegeki
--

ALTER TABLE ONLY public.platform
    ADD CONSTRAINT platform_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.category(id);


--
-- PostgreSQL database dump complete
--

