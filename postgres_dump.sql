--
-- PostgreSQL database dump
--

-- Dumped from database version 11.9 (Debian 11.9-0+deb10u1)
-- Dumped by pg_dump version 11.9 (Debian 11.9-0+deb10u1)

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: accounts_userprofile; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.accounts_userprofile (
    id integer NOT NULL,
    user_id integer NOT NULL,
    audience integer,
    email_correspondance_ok boolean NOT NULL
);


ALTER TABLE public.accounts_userprofile OWNER TO wgg;

--
-- Name: accounts_userprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.accounts_userprofile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accounts_userprofile_id_seq OWNER TO wgg;

--
-- Name: accounts_userprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.accounts_userprofile_id_seq OWNED BY public.accounts_userprofile.id;


--
-- Name: articles_article; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.articles_article (
    id integer NOT NULL,
    link character varying(255) NOT NULL,
    redirect_link character varying(255),
    main_image_source character varying(1000),
    content text,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    redirects boolean,
    content_links text,
    content_links_count integer,
    content_size integer,
    outbound_links character varying(255)[],
    inbound_links character varying(255)[],
    description character varying(255),
    sections_count integer
);


ALTER TABLE public.articles_article OWNER TO wgg;

--
-- Name: articles_article_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.articles_article_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.articles_article_id_seq OWNER TO wgg;

--
-- Name: articles_article_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.articles_article_id_seq OWNED BY public.articles_article.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO wgg;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO wgg;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO wgg;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO wgg;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO wgg;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO wgg;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO wgg;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO wgg;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO wgg;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO wgg;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO wgg;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO wgg;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO wgg;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO wgg;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO wgg;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO wgg;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: game_challengearticle; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.game_challengearticle (
    id integer NOT NULL,
    "position" integer NOT NULL,
    "order" integer NOT NULL,
    added timestamp with time zone NOT NULL,
    article_id integer NOT NULL,
    challenge_article_list_id integer NOT NULL,
    CONSTRAINT game_challengearticle_order_47481101_check CHECK (("order" >= 0))
);


ALTER TABLE public.game_challengearticle OWNER TO wgg;

--
-- Name: game_challengearticle_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.game_challengearticle_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_challengearticle_id_seq OWNER TO wgg;

--
-- Name: game_challengearticle_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.game_challengearticle_id_seq OWNED BY public.game_challengearticle.id;


--
-- Name: game_challengearticlelist; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.game_challengearticlelist (
    id integer NOT NULL,
    name character varying(255),
    public boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    creator_id integer,
    group_id integer
);


ALTER TABLE public.game_challengearticlelist OWNER TO wgg;

--
-- Name: game_challengearticlelist_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.game_challengearticlelist_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_challengearticlelist_id_seq OWNER TO wgg;

--
-- Name: game_challengearticlelist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.game_challengearticlelist_id_seq OWNED BY public.game_challengearticlelist.id;


--
-- Name: game_challengeset; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.game_challengeset (
    id integer NOT NULL,
    name character varying(255),
    "default" boolean NOT NULL,
    public boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    creator_id integer,
    group_id integer
);


ALTER TABLE public.game_challengeset OWNER TO wgg;

--
-- Name: game_challengeset_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.game_challengeset_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_challengeset_id_seq OWNER TO wgg;

--
-- Name: game_challengeset_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.game_challengeset_id_seq OWNED BY public.game_challengeset.id;


--
-- Name: game_challengesetchallenge; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.game_challengesetchallenge (
    id integer NOT NULL,
    "order" integer NOT NULL,
    added timestamp with time zone NOT NULL,
    challenge_id integer NOT NULL,
    challenge_set_id integer NOT NULL,
    CONSTRAINT game_challengesetchallenge_order_c21c0f72_check CHECK (("order" >= 0))
);


ALTER TABLE public.game_challengesetchallenge OWNER TO wgg;

--
-- Name: game_challengesetchallenge_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.game_challengesetchallenge_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_challengesetchallenge_id_seq OWNER TO wgg;

--
-- Name: game_challengesetchallenge_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.game_challengesetchallenge_id_seq OWNED BY public.game_challengesetchallenge.id;


--
-- Name: game_click; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.game_click (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    article_id integer NOT NULL,
    game_id integer NOT NULL
);


ALTER TABLE public.game_click OWNER TO wgg;

--
-- Name: game_click_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.game_click_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_click_id_seq OWNER TO wgg;

--
-- Name: game_click_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.game_click_id_seq OWNED BY public.game_click.id;


--
-- Name: game_game; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.game_game (
    id integer NOT NULL,
    won boolean NOT NULL,
    points integer,
    total_time integer,
    created timestamp with time zone NOT NULL,
    player_id integer NOT NULL,
    round_id integer NOT NULL
);


ALTER TABLE public.game_game OWNER TO wgg;

--
-- Name: game_game_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.game_game_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_game_id_seq OWNER TO wgg;

--
-- Name: game_game_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.game_game_id_seq OWNED BY public.game_game.id;


--
-- Name: game_groupchallenge; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.game_groupchallenge (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    creator_id integer,
    goal_article_id integer NOT NULL,
    group_id integer NOT NULL,
    start_article_id integer NOT NULL
);


ALTER TABLE public.game_groupchallenge OWNER TO wgg;

--
-- Name: game_groupchallenge_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.game_groupchallenge_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_groupchallenge_id_seq OWNER TO wgg;

--
-- Name: game_groupchallenge_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.game_groupchallenge_id_seq OWNED BY public.game_groupchallenge.id;


--
-- Name: game_round; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.game_round (
    id integer NOT NULL,
    mode integer NOT NULL,
    start_time timestamp with time zone NOT NULL,
    max_time integer NOT NULL,
    created timestamp with time zone NOT NULL,
    group_id integer NOT NULL,
    pre_round_wait_time integer NOT NULL,
    challenge_id integer,
    active boolean NOT NULL
);


ALTER TABLE public.game_round OWNER TO wgg;

--
-- Name: game_round_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.game_round_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_round_id_seq OWNER TO wgg;

--
-- Name: game_round_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.game_round_id_seq OWNED BY public.game_round.id;


--
-- Name: game_roundchallenge; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.game_roundchallenge (
    id integer NOT NULL,
    creator_id integer,
    goal_article_id integer NOT NULL,
    group_challenge_id integer,
    start_article_id integer NOT NULL
);


ALTER TABLE public.game_roundchallenge OWNER TO wgg;

--
-- Name: game_roundchallenge_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.game_roundchallenge_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_roundchallenge_id_seq OWNER TO wgg;

--
-- Name: game_roundchallenge_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.game_roundchallenge_id_seq OWNED BY public.game_roundchallenge.id;


--
-- Name: group_group; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.group_group (
    id integer NOT NULL,
    name character varying(255),
    short_code integer NOT NULL,
    long_code uuid NOT NULL,
    auto_start_new_round boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    pre_round_wait_time integer NOT NULL,
    round_max_time integer NOT NULL,
    new_round_uses_random_challenge boolean NOT NULL,
    local_timezone integer NOT NULL,
    play_sounds boolean NOT NULL,
    active_challenge_article_list_id integer,
    active_challenge_set_id integer
);


ALTER TABLE public.group_group OWNER TO wgg;

--
-- Name: group_group_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.group_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.group_group_id_seq OWNER TO wgg;

--
-- Name: group_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.group_group_id_seq OWNED BY public.group_group.id;


--
-- Name: group_groupmembership; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.group_groupmembership (
    id integer NOT NULL,
    member_name character varying(255),
    is_admin boolean NOT NULL,
    joined timestamp with time zone NOT NULL,
    group_id integer NOT NULL,
    user_id integer NOT NULL,
    is_guest boolean NOT NULL
);


ALTER TABLE public.group_groupmembership OWNER TO wgg;

--
-- Name: group_groupmembership_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.group_groupmembership_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.group_groupmembership_id_seq OWNER TO wgg;

--
-- Name: group_groupmembership_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.group_groupmembership_id_seq OWNED BY public.group_groupmembership.id;


--
-- Name: stats_points; Type: TABLE; Schema: public; Owner: wgg
--

CREATE TABLE public.stats_points (
    id integer NOT NULL,
    day_points integer NOT NULL,
    day_points_last_update timestamp with time zone NOT NULL,
    week_points integer NOT NULL,
    week_points_last_update timestamp with time zone NOT NULL,
    all_points integer NOT NULL,
    group_id integer NOT NULL,
    player_id integer NOT NULL
);


ALTER TABLE public.stats_points OWNER TO wgg;

--
-- Name: stats_points_id_seq; Type: SEQUENCE; Schema: public; Owner: wgg
--

CREATE SEQUENCE public.stats_points_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stats_points_id_seq OWNER TO wgg;

--
-- Name: stats_points_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wgg
--

ALTER SEQUENCE public.stats_points_id_seq OWNED BY public.stats_points.id;


--
-- Name: accounts_userprofile id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.accounts_userprofile ALTER COLUMN id SET DEFAULT nextval('public.accounts_userprofile_id_seq'::regclass);


--
-- Name: articles_article id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.articles_article ALTER COLUMN id SET DEFAULT nextval('public.articles_article_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: game_challengearticle id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengearticle ALTER COLUMN id SET DEFAULT nextval('public.game_challengearticle_id_seq'::regclass);


--
-- Name: game_challengearticlelist id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengearticlelist ALTER COLUMN id SET DEFAULT nextval('public.game_challengearticlelist_id_seq'::regclass);


--
-- Name: game_challengeset id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengeset ALTER COLUMN id SET DEFAULT nextval('public.game_challengeset_id_seq'::regclass);


--
-- Name: game_challengesetchallenge id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengesetchallenge ALTER COLUMN id SET DEFAULT nextval('public.game_challengesetchallenge_id_seq'::regclass);


--
-- Name: game_click id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_click ALTER COLUMN id SET DEFAULT nextval('public.game_click_id_seq'::regclass);


--
-- Name: game_game id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_game ALTER COLUMN id SET DEFAULT nextval('public.game_game_id_seq'::regclass);


--
-- Name: game_groupchallenge id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_groupchallenge ALTER COLUMN id SET DEFAULT nextval('public.game_groupchallenge_id_seq'::regclass);


--
-- Name: game_round id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_round ALTER COLUMN id SET DEFAULT nextval('public.game_round_id_seq'::regclass);


--
-- Name: game_roundchallenge id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_roundchallenge ALTER COLUMN id SET DEFAULT nextval('public.game_roundchallenge_id_seq'::regclass);


--
-- Name: group_group id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.group_group ALTER COLUMN id SET DEFAULT nextval('public.group_group_id_seq'::regclass);


--
-- Name: group_groupmembership id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.group_groupmembership ALTER COLUMN id SET DEFAULT nextval('public.group_groupmembership_id_seq'::regclass);


--
-- Name: stats_points id; Type: DEFAULT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.stats_points ALTER COLUMN id SET DEFAULT nextval('public.stats_points_id_seq'::regclass);


--
-- Name: articles_article articles_article_link_key; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.articles_article
    ADD CONSTRAINT articles_article_link_key UNIQUE (link);


--
-- Name: articles_article articles_article_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.articles_article
    ADD CONSTRAINT articles_article_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: game_challengearticle game_challengearticle_article_id_challenge_art_27f95cd8_uniq; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengearticle
    ADD CONSTRAINT game_challengearticle_article_id_challenge_art_27f95cd8_uniq UNIQUE (article_id, challenge_article_list_id);


--
-- Name: game_challengearticle game_challengearticle_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengearticle
    ADD CONSTRAINT game_challengearticle_pkey PRIMARY KEY (id);


--
-- Name: game_challengearticlelist game_challengearticlelist_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengearticlelist
    ADD CONSTRAINT game_challengearticlelist_pkey PRIMARY KEY (id);


--
-- Name: game_challengeset game_challengeset_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengeset
    ADD CONSTRAINT game_challengeset_pkey PRIMARY KEY (id);


--
-- Name: game_challengesetchallenge game_challengesetchallen_challenge_id_challenge_s_1be76da6_uniq; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengesetchallenge
    ADD CONSTRAINT game_challengesetchallen_challenge_id_challenge_s_1be76da6_uniq UNIQUE (challenge_id, challenge_set_id);


--
-- Name: game_challengesetchallenge game_challengesetchallenge_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengesetchallenge
    ADD CONSTRAINT game_challengesetchallenge_pkey PRIMARY KEY (id);


--
-- Name: game_click game_click_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_click
    ADD CONSTRAINT game_click_pkey PRIMARY KEY (id);


--
-- Name: game_game game_game_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_game
    ADD CONSTRAINT game_game_pkey PRIMARY KEY (id);


--
-- Name: game_groupchallenge game_groupchallenge_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_groupchallenge
    ADD CONSTRAINT game_groupchallenge_pkey PRIMARY KEY (id);


--
-- Name: game_round game_round_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_round
    ADD CONSTRAINT game_round_pkey PRIMARY KEY (id);


--
-- Name: game_roundchallenge game_roundchallenge_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_roundchallenge
    ADD CONSTRAINT game_roundchallenge_pkey PRIMARY KEY (id);


--
-- Name: group_group group_group_active_challenge_article_list_id_key; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.group_group
    ADD CONSTRAINT group_group_active_challenge_article_list_id_key UNIQUE (active_challenge_article_list_id);


--
-- Name: group_group group_group_active_challenge_set_id_key; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.group_group
    ADD CONSTRAINT group_group_active_challenge_set_id_key UNIQUE (active_challenge_set_id);


--
-- Name: group_group group_group_long_code_key; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.group_group
    ADD CONSTRAINT group_group_long_code_key UNIQUE (long_code);


--
-- Name: group_group group_group_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.group_group
    ADD CONSTRAINT group_group_pkey PRIMARY KEY (id);


--
-- Name: group_group group_group_short_code_key; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.group_group
    ADD CONSTRAINT group_group_short_code_key UNIQUE (short_code);


--
-- Name: group_groupmembership group_groupmembership_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.group_groupmembership
    ADD CONSTRAINT group_groupmembership_pkey PRIMARY KEY (id);


--
-- Name: group_groupmembership group_groupmembership_user_id_group_id_55842044_uniq; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.group_groupmembership
    ADD CONSTRAINT group_groupmembership_user_id_group_id_55842044_uniq UNIQUE (user_id, group_id);


--
-- Name: stats_points stats_points_pkey; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.stats_points
    ADD CONSTRAINT stats_points_pkey PRIMARY KEY (id);


--
-- Name: stats_points stats_points_player_id_group_id_34d98a6a_uniq; Type: CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.stats_points
    ADD CONSTRAINT stats_points_player_id_group_id_34d98a6a_uniq UNIQUE (player_id, group_id);


--
-- Name: articles_article_link_5d927c22_like; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX articles_article_link_5d927c22_like ON public.articles_article USING btree (link varchar_pattern_ops);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: game_challengearticle_article_id_2b54d276; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_challengearticle_article_id_2b54d276 ON public.game_challengearticle USING btree (article_id);


--
-- Name: game_challengearticle_challenge_article_list_id_0a3d8d2e; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_challengearticle_challenge_article_list_id_0a3d8d2e ON public.game_challengearticle USING btree (challenge_article_list_id);


--
-- Name: game_challengearticlelist_creator_id_63a4c8d0; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_challengearticlelist_creator_id_63a4c8d0 ON public.game_challengearticlelist USING btree (creator_id);


--
-- Name: game_challengearticlelist_group_id_10b9336e; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_challengearticlelist_group_id_10b9336e ON public.game_challengearticlelist USING btree (group_id);


--
-- Name: game_challengeset_creator_id_534d9734; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_challengeset_creator_id_534d9734 ON public.game_challengeset USING btree (creator_id);


--
-- Name: game_challengeset_group_id_fb512070; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_challengeset_group_id_fb512070 ON public.game_challengeset USING btree (group_id);


--
-- Name: game_challengesetchallenge_challenge_id_635d440f; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_challengesetchallenge_challenge_id_635d440f ON public.game_challengesetchallenge USING btree (challenge_id);


--
-- Name: game_challengesetchallenge_challenge_set_id_643f8ec6; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_challengesetchallenge_challenge_set_id_643f8ec6 ON public.game_challengesetchallenge USING btree (challenge_set_id);


--
-- Name: game_click_article_id_04cb4487; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_click_article_id_04cb4487 ON public.game_click USING btree (article_id);


--
-- Name: game_click_created_48e518d6; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_click_created_48e518d6 ON public.game_click USING btree (created);


--
-- Name: game_click_game_id_a6bb08ab; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_click_game_id_a6bb08ab ON public.game_click USING btree (game_id);


--
-- Name: game_game_player_id_cfeb1674; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_game_player_id_cfeb1674 ON public.game_game USING btree (player_id);


--
-- Name: game_game_round_id_d3619f7f; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_game_round_id_d3619f7f ON public.game_game USING btree (round_id);


--
-- Name: game_groupchallenge_creator_id_fd5ecc89; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_groupchallenge_creator_id_fd5ecc89 ON public.game_groupchallenge USING btree (creator_id);


--
-- Name: game_groupchallenge_goal_article_id_e3a3f3dc; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_groupchallenge_goal_article_id_e3a3f3dc ON public.game_groupchallenge USING btree (goal_article_id);


--
-- Name: game_groupchallenge_group_id_ce26d34f; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_groupchallenge_group_id_ce26d34f ON public.game_groupchallenge USING btree (group_id);


--
-- Name: game_groupchallenge_start_article_id_eb42c6aa; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_groupchallenge_start_article_id_eb42c6aa ON public.game_groupchallenge USING btree (start_article_id);


--
-- Name: game_round_created_56c67248; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_round_created_56c67248 ON public.game_round USING btree (created);


--
-- Name: game_round_group_id_9c8cc159; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_round_group_id_9c8cc159 ON public.game_round USING btree (group_id);


--
-- Name: game_round_round_challenge_id_cf8bf32a; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_round_round_challenge_id_cf8bf32a ON public.game_round USING btree (challenge_id);


--
-- Name: game_roundchallenge_creator_id_f9c4ca88; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_roundchallenge_creator_id_f9c4ca88 ON public.game_roundchallenge USING btree (creator_id);


--
-- Name: game_roundchallenge_goal_article_id_3fa78d54; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_roundchallenge_goal_article_id_3fa78d54 ON public.game_roundchallenge USING btree (goal_article_id);


--
-- Name: game_roundchallenge_group_challenge_id_161cdc0e; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_roundchallenge_group_challenge_id_161cdc0e ON public.game_roundchallenge USING btree (group_challenge_id);


--
-- Name: game_roundchallenge_start_article_id_6a98ab3b; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX game_roundchallenge_start_article_id_6a98ab3b ON public.game_roundchallenge USING btree (start_article_id);


--
-- Name: group_groupmembership_group_id_af476011; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX group_groupmembership_group_id_af476011 ON public.group_groupmembership USING btree (group_id);


--
-- Name: group_groupmembership_user_id_8768dc01; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX group_groupmembership_user_id_8768dc01 ON public.group_groupmembership USING btree (user_id);


--
-- Name: stats_points_all_points_1c47f917; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX stats_points_all_points_1c47f917 ON public.stats_points USING btree (all_points);


--
-- Name: stats_points_day_points_2c367743; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX stats_points_day_points_2c367743 ON public.stats_points USING btree (day_points);


--
-- Name: stats_points_group_id_35c25ed2; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX stats_points_group_id_35c25ed2 ON public.stats_points USING btree (group_id);


--
-- Name: stats_points_player_id_e9f9df83; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX stats_points_player_id_e9f9df83 ON public.stats_points USING btree (player_id);


--
-- Name: stats_points_week_points_b8efdcaa; Type: INDEX; Schema: public; Owner: wgg
--

CREATE INDEX stats_points_week_points_b8efdcaa ON public.stats_points USING btree (week_points);


--
-- Name: accounts_userprofile accounts_userprofile_user_id_92240672_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.accounts_userprofile
    ADD CONSTRAINT accounts_userprofile_user_id_92240672_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_challengearticle game_challengearticl_article_id_2b54d276_fk_articles_; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengearticle
    ADD CONSTRAINT game_challengearticl_article_id_2b54d276_fk_articles_ FOREIGN KEY (article_id) REFERENCES public.articles_article(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_challengearticle game_challengearticl_challenge_article_li_0a3d8d2e_fk_game_chal; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengearticle
    ADD CONSTRAINT game_challengearticl_challenge_article_li_0a3d8d2e_fk_game_chal FOREIGN KEY (challenge_article_list_id) REFERENCES public.game_challengearticlelist(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_challengearticlelist game_challengearticlelist_creator_id_63a4c8d0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengearticlelist
    ADD CONSTRAINT game_challengearticlelist_creator_id_63a4c8d0_fk_auth_user_id FOREIGN KEY (creator_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_challengearticlelist game_challengearticlelist_group_id_10b9336e_fk_group_group_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengearticlelist
    ADD CONSTRAINT game_challengearticlelist_group_id_10b9336e_fk_group_group_id FOREIGN KEY (group_id) REFERENCES public.group_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_challengeset game_challengeset_creator_id_534d9734_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengeset
    ADD CONSTRAINT game_challengeset_creator_id_534d9734_fk_auth_user_id FOREIGN KEY (creator_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_challengeset game_challengeset_group_id_fb512070_fk_group_group_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengeset
    ADD CONSTRAINT game_challengeset_group_id_fb512070_fk_group_group_id FOREIGN KEY (group_id) REFERENCES public.group_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_challengesetchallenge game_challengesetcha_challenge_id_635d440f_fk_game_grou; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengesetchallenge
    ADD CONSTRAINT game_challengesetcha_challenge_id_635d440f_fk_game_grou FOREIGN KEY (challenge_id) REFERENCES public.game_groupchallenge(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_challengesetchallenge game_challengesetcha_challenge_set_id_643f8ec6_fk_game_chal; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_challengesetchallenge
    ADD CONSTRAINT game_challengesetcha_challenge_set_id_643f8ec6_fk_game_chal FOREIGN KEY (challenge_set_id) REFERENCES public.game_challengeset(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_click game_click_article_id_04cb4487_fk_articles_article_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_click
    ADD CONSTRAINT game_click_article_id_04cb4487_fk_articles_article_id FOREIGN KEY (article_id) REFERENCES public.articles_article(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_click game_click_game_id_a6bb08ab_fk_game_game_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_click
    ADD CONSTRAINT game_click_game_id_a6bb08ab_fk_game_game_id FOREIGN KEY (game_id) REFERENCES public.game_game(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_game game_game_player_id_cfeb1674_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_game
    ADD CONSTRAINT game_game_player_id_cfeb1674_fk_auth_user_id FOREIGN KEY (player_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_game game_game_round_id_d3619f7f_fk_game_round_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_game
    ADD CONSTRAINT game_game_round_id_d3619f7f_fk_game_round_id FOREIGN KEY (round_id) REFERENCES public.game_round(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_groupchallenge game_groupchallenge_creator_id_fd5ecc89_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_groupchallenge
    ADD CONSTRAINT game_groupchallenge_creator_id_fd5ecc89_fk_auth_user_id FOREIGN KEY (creator_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_groupchallenge game_groupchallenge_goal_article_id_e3a3f3dc_fk_articles_; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_groupchallenge
    ADD CONSTRAINT game_groupchallenge_goal_article_id_e3a3f3dc_fk_articles_ FOREIGN KEY (goal_article_id) REFERENCES public.articles_article(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_groupchallenge game_groupchallenge_group_id_ce26d34f_fk_group_group_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_groupchallenge
    ADD CONSTRAINT game_groupchallenge_group_id_ce26d34f_fk_group_group_id FOREIGN KEY (group_id) REFERENCES public.group_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_groupchallenge game_groupchallenge_start_article_id_eb42c6aa_fk_articles_; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_groupchallenge
    ADD CONSTRAINT game_groupchallenge_start_article_id_eb42c6aa_fk_articles_ FOREIGN KEY (start_article_id) REFERENCES public.articles_article(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_round game_round_challenge_id_6e0296a2_fk_game_roundchallenge_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_round
    ADD CONSTRAINT game_round_challenge_id_6e0296a2_fk_game_roundchallenge_id FOREIGN KEY (challenge_id) REFERENCES public.game_roundchallenge(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_round game_round_group_id_9c8cc159_fk_group_group_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_round
    ADD CONSTRAINT game_round_group_id_9c8cc159_fk_group_group_id FOREIGN KEY (group_id) REFERENCES public.group_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_roundchallenge game_roundchallenge_creator_id_f9c4ca88_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_roundchallenge
    ADD CONSTRAINT game_roundchallenge_creator_id_f9c4ca88_fk_auth_user_id FOREIGN KEY (creator_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_roundchallenge game_roundchallenge_goal_article_id_3fa78d54_fk_articles_; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_roundchallenge
    ADD CONSTRAINT game_roundchallenge_goal_article_id_3fa78d54_fk_articles_ FOREIGN KEY (goal_article_id) REFERENCES public.articles_article(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_roundchallenge game_roundchallenge_group_challenge_id_161cdc0e_fk_game_grou; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_roundchallenge
    ADD CONSTRAINT game_roundchallenge_group_challenge_id_161cdc0e_fk_game_grou FOREIGN KEY (group_challenge_id) REFERENCES public.game_groupchallenge(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: game_roundchallenge game_roundchallenge_start_article_id_6a98ab3b_fk_articles_; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.game_roundchallenge
    ADD CONSTRAINT game_roundchallenge_start_article_id_6a98ab3b_fk_articles_ FOREIGN KEY (start_article_id) REFERENCES public.articles_article(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_group group_group_active_challenge_art_f3cbfee2_fk_game_chal; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.group_group
    ADD CONSTRAINT group_group_active_challenge_art_f3cbfee2_fk_game_chal FOREIGN KEY (active_challenge_article_list_id) REFERENCES public.game_challengearticlelist(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_group group_group_active_challenge_set_214d336c_fk_game_chal; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.group_group
    ADD CONSTRAINT group_group_active_challenge_set_214d336c_fk_game_chal FOREIGN KEY (active_challenge_set_id) REFERENCES public.game_challengeset(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_groupmembership group_groupmembership_group_id_af476011_fk_group_group_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.group_groupmembership
    ADD CONSTRAINT group_groupmembership_group_id_af476011_fk_group_group_id FOREIGN KEY (group_id) REFERENCES public.group_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_groupmembership group_groupmembership_user_id_8768dc01_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.group_groupmembership
    ADD CONSTRAINT group_groupmembership_user_id_8768dc01_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: stats_points stats_points_group_id_35c25ed2_fk_group_group_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.stats_points
    ADD CONSTRAINT stats_points_group_id_35c25ed2_fk_group_group_id FOREIGN KEY (group_id) REFERENCES public.group_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: stats_points stats_points_player_id_e9f9df83_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: wgg
--

ALTER TABLE ONLY public.stats_points
    ADD CONSTRAINT stats_points_player_id_e9f9df83_fk_auth_user_id FOREIGN KEY (player_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

