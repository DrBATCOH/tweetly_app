--
-- PostgreSQL database dump
--

-- Dumped from database version 14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)

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

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO tw_user;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO tw_user;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO tw_user;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: comments; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.comments (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    content character varying(100) NOT NULL,
    tweet_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.comments OWNER TO tw_user;

--
-- Name: comments_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.comments ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.comments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: country; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.country (
    id bigint NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE public.country OWNER TO tw_user;

--
-- Name: country_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.country ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.country_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: custom_user; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.custom_user (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    status character varying(20) NOT NULL,
    email character varying(35) NOT NULL,
    avatar character varying(100) NOT NULL,
    country character varying(100) NOT NULL,
    birthdate date NOT NULL
);


ALTER TABLE public.custom_user OWNER TO tw_user;

--
-- Name: custom_user_groups; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.custom_user_groups (
    id bigint NOT NULL,
    customuser_id bigint NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.custom_user_groups OWNER TO tw_user;

--
-- Name: custom_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.custom_user_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.custom_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: custom_user_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.custom_user ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.custom_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: custom_user_user_permissions; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.custom_user_user_permissions (
    id bigint NOT NULL,
    customuser_id bigint NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.custom_user_user_permissions OWNER TO tw_user;

--
-- Name: custom_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.custom_user_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.custom_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO tw_user;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO tw_user;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO tw_user;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO tw_user;

--
-- Name: email_codes; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.email_codes (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    code character varying(100) NOT NULL,
    expiration integer NOT NULL,
    user_id bigint NOT NULL,
    CONSTRAINT email_codes_expiration_check CHECK ((expiration >= 0))
);


ALTER TABLE public.email_codes OWNER TO tw_user;

--
-- Name: email_codes_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.email_codes ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.email_codes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: followers; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.followers (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    follower_id bigint NOT NULL,
    following_id bigint NOT NULL
);


ALTER TABLE public.followers OWNER TO tw_user;

--
-- Name: followers_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.followers ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.followers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: likes; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.likes (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.likes OWNER TO tw_user;

--
-- Name: likes_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.likes ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.likes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: notifications; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.notifications (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    message character varying(255) NOT NULL,
    is_real boolean NOT NULL
);


ALTER TABLE public.notifications OWNER TO tw_user;

--
-- Name: notifications_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.notifications ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.notifications_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: retweets; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.retweets (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.retweets OWNER TO tw_user;

--
-- Name: retweets_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.retweets ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.retweets_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: tags; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.tags (
    id bigint NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE public.tags OWNER TO tw_user;

--
-- Name: tags_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.tags ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: tweet_comment; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.tweet_comment (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    comment_id bigint NOT NULL,
    tweet_id bigint NOT NULL
);


ALTER TABLE public.tweet_comment OWNER TO tw_user;

--
-- Name: tweet_comment_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.tweet_comment ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.tweet_comment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: tweet_like; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.tweet_like (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    like_id bigint NOT NULL,
    tweet_id bigint NOT NULL
);


ALTER TABLE public.tweet_like OWNER TO tw_user;

--
-- Name: tweet_like_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.tweet_like ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.tweet_like_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: tweet_tag; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.tweet_tag (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    tag_id bigint NOT NULL,
    tweet_id bigint NOT NULL
);


ALTER TABLE public.tweet_tag OWNER TO tw_user;

--
-- Name: tweet_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.tweet_tag ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.tweet_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: tweets; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.tweets (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    content text NOT NULL,
    author_id bigint NOT NULL
);


ALTER TABLE public.tweets OWNER TO tw_user;

--
-- Name: tweets_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.tweets ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.tweets_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: users_notifications; Type: TABLE; Schema: public; Owner: tw_user
--

CREATE TABLE public.users_notifications (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    notification_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.users_notifications OWNER TO tw_user;

--
-- Name: users_notifications_id_seq; Type: SEQUENCE; Schema: public; Owner: tw_user
--

ALTER TABLE public.users_notifications ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.users_notifications_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: comments comments_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (id);


--
-- Name: country country_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.country
    ADD CONSTRAINT country_pkey PRIMARY KEY (id);


--
-- Name: custom_user custom_user_email_key; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.custom_user
    ADD CONSTRAINT custom_user_email_key UNIQUE (email);


--
-- Name: custom_user_groups custom_user_groups_customuser_id_group_id_ea14f886_uniq; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.custom_user_groups
    ADD CONSTRAINT custom_user_groups_customuser_id_group_id_ea14f886_uniq UNIQUE (customuser_id, group_id);


--
-- Name: custom_user_groups custom_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.custom_user_groups
    ADD CONSTRAINT custom_user_groups_pkey PRIMARY KEY (id);


--
-- Name: custom_user custom_user_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.custom_user
    ADD CONSTRAINT custom_user_pkey PRIMARY KEY (id);


--
-- Name: custom_user_user_permissions custom_user_user_permiss_customuser_id_permission_f9232336_uniq; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.custom_user_user_permissions
    ADD CONSTRAINT custom_user_user_permiss_customuser_id_permission_f9232336_uniq UNIQUE (customuser_id, permission_id);


--
-- Name: custom_user_user_permissions custom_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.custom_user_user_permissions
    ADD CONSTRAINT custom_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: custom_user custom_user_username_key; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.custom_user
    ADD CONSTRAINT custom_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: email_codes email_codes_code_key; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.email_codes
    ADD CONSTRAINT email_codes_code_key UNIQUE (code);


--
-- Name: email_codes email_codes_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.email_codes
    ADD CONSTRAINT email_codes_pkey PRIMARY KEY (id);


--
-- Name: followers followers_follower_id_following_id_79c3974a_uniq; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.followers
    ADD CONSTRAINT followers_follower_id_following_id_79c3974a_uniq UNIQUE (follower_id, following_id);


--
-- Name: followers followers_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.followers
    ADD CONSTRAINT followers_pkey PRIMARY KEY (id);


--
-- Name: likes likes_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_pkey PRIMARY KEY (id);


--
-- Name: notifications notifications_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_pkey PRIMARY KEY (id);


--
-- Name: retweets retweets_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.retweets
    ADD CONSTRAINT retweets_pkey PRIMARY KEY (id);


--
-- Name: tags tags_name_key; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_name_key UNIQUE (name);


--
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (id);


--
-- Name: tweet_comment tweet_comment_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.tweet_comment
    ADD CONSTRAINT tweet_comment_pkey PRIMARY KEY (id);


--
-- Name: tweet_like tweet_like_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.tweet_like
    ADD CONSTRAINT tweet_like_pkey PRIMARY KEY (id);


--
-- Name: tweet_tag tweet_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.tweet_tag
    ADD CONSTRAINT tweet_tag_pkey PRIMARY KEY (id);


--
-- Name: tweets tweets_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.tweets
    ADD CONSTRAINT tweets_pkey PRIMARY KEY (id);


--
-- Name: users_notifications users_notifications_pkey; Type: CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.users_notifications
    ADD CONSTRAINT users_notifications_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: comments_tweet_id_dcb840dd; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX comments_tweet_id_dcb840dd ON public.comments USING btree (tweet_id);


--
-- Name: comments_user_id_b8fd0b64; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX comments_user_id_b8fd0b64 ON public.comments USING btree (user_id);


--
-- Name: custom_user_email_54654c31_like; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX custom_user_email_54654c31_like ON public.custom_user USING btree (email varchar_pattern_ops);


--
-- Name: custom_user_groups_customuser_id_8e3d0338; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX custom_user_groups_customuser_id_8e3d0338 ON public.custom_user_groups USING btree (customuser_id);


--
-- Name: custom_user_groups_group_id_02874f21; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX custom_user_groups_group_id_02874f21 ON public.custom_user_groups USING btree (group_id);


--
-- Name: custom_user_user_permissions_customuser_id_ec2da4cb; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX custom_user_user_permissions_customuser_id_ec2da4cb ON public.custom_user_user_permissions USING btree (customuser_id);


--
-- Name: custom_user_user_permissions_permission_id_f82b5e3f; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX custom_user_user_permissions_permission_id_f82b5e3f ON public.custom_user_user_permissions USING btree (permission_id);


--
-- Name: custom_user_username_5f1e8aad_like; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX custom_user_username_5f1e8aad_like ON public.custom_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: email_codes_code_06c36ba8_like; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX email_codes_code_06c36ba8_like ON public.email_codes USING btree (code varchar_pattern_ops);


--
-- Name: email_codes_user_id_4dc2581f; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX email_codes_user_id_4dc2581f ON public.email_codes USING btree (user_id);


--
-- Name: followers_follower_id_d0672679; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX followers_follower_id_d0672679 ON public.followers USING btree (follower_id);


--
-- Name: followers_following_id_b364b5a6; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX followers_following_id_b364b5a6 ON public.followers USING btree (following_id);


--
-- Name: likes_tweet_id_358e07ab; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX likes_tweet_id_358e07ab ON public.likes USING btree (tweet_id);


--
-- Name: likes_user_id_0899754c; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX likes_user_id_0899754c ON public.likes USING btree (user_id);


--
-- Name: retweets_tweet_id_ac1e30c4; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX retweets_tweet_id_ac1e30c4 ON public.retweets USING btree (tweet_id);


--
-- Name: retweets_user_id_e6648b88; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX retweets_user_id_e6648b88 ON public.retweets USING btree (user_id);


--
-- Name: tags_name_d06e0d9e_like; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX tags_name_d06e0d9e_like ON public.tags USING btree (name varchar_pattern_ops);


--
-- Name: tweet_comment_comment_id_ab9de2c6; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX tweet_comment_comment_id_ab9de2c6 ON public.tweet_comment USING btree (comment_id);


--
-- Name: tweet_comment_tweet_id_b7e029aa; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX tweet_comment_tweet_id_b7e029aa ON public.tweet_comment USING btree (tweet_id);


--
-- Name: tweet_like_like_id_611f14fd; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX tweet_like_like_id_611f14fd ON public.tweet_like USING btree (like_id);


--
-- Name: tweet_like_tweet_id_270cb5ec; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX tweet_like_tweet_id_270cb5ec ON public.tweet_like USING btree (tweet_id);


--
-- Name: tweet_tag_tag_id_eb4437db; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX tweet_tag_tag_id_eb4437db ON public.tweet_tag USING btree (tag_id);


--
-- Name: tweet_tag_tweet_id_317b1f42; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX tweet_tag_tweet_id_317b1f42 ON public.tweet_tag USING btree (tweet_id);


--
-- Name: tweets_author_id_2519aa0a; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX tweets_author_id_2519aa0a ON public.tweets USING btree (author_id);


--
-- Name: users_notifications_notification_id_97b59280; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX users_notifications_notification_id_97b59280 ON public.users_notifications USING btree (notification_id);


--
-- Name: users_notifications_user_id_d8bb60d3; Type: INDEX; Schema: public; Owner: tw_user
--

CREATE INDEX users_notifications_user_id_d8bb60d3 ON public.users_notifications USING btree (user_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: comments comments_tweet_id_dcb840dd_fk_tweets_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_tweet_id_dcb840dd_fk_tweets_id FOREIGN KEY (tweet_id) REFERENCES public.tweets(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: comments comments_user_id_b8fd0b64_fk_custom_user_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_user_id_b8fd0b64_fk_custom_user_id FOREIGN KEY (user_id) REFERENCES public.custom_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: custom_user_groups custom_user_groups_customuser_id_8e3d0338_fk_custom_user_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.custom_user_groups
    ADD CONSTRAINT custom_user_groups_customuser_id_8e3d0338_fk_custom_user_id FOREIGN KEY (customuser_id) REFERENCES public.custom_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: custom_user_groups custom_user_groups_group_id_02874f21_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.custom_user_groups
    ADD CONSTRAINT custom_user_groups_group_id_02874f21_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: custom_user_user_permissions custom_user_user_per_customuser_id_ec2da4cb_fk_custom_us; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.custom_user_user_permissions
    ADD CONSTRAINT custom_user_user_per_customuser_id_ec2da4cb_fk_custom_us FOREIGN KEY (customuser_id) REFERENCES public.custom_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: custom_user_user_permissions custom_user_user_per_permission_id_f82b5e3f_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.custom_user_user_permissions
    ADD CONSTRAINT custom_user_user_per_permission_id_f82b5e3f_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_custom_user_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_custom_user_id FOREIGN KEY (user_id) REFERENCES public.custom_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: email_codes email_codes_user_id_4dc2581f_fk_custom_user_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.email_codes
    ADD CONSTRAINT email_codes_user_id_4dc2581f_fk_custom_user_id FOREIGN KEY (user_id) REFERENCES public.custom_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: followers followers_follower_id_d0672679_fk_custom_user_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.followers
    ADD CONSTRAINT followers_follower_id_d0672679_fk_custom_user_id FOREIGN KEY (follower_id) REFERENCES public.custom_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: followers followers_following_id_b364b5a6_fk_custom_user_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.followers
    ADD CONSTRAINT followers_following_id_b364b5a6_fk_custom_user_id FOREIGN KEY (following_id) REFERENCES public.custom_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: likes likes_tweet_id_358e07ab_fk_tweets_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_tweet_id_358e07ab_fk_tweets_id FOREIGN KEY (tweet_id) REFERENCES public.tweets(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: likes likes_user_id_0899754c_fk_custom_user_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_user_id_0899754c_fk_custom_user_id FOREIGN KEY (user_id) REFERENCES public.custom_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: retweets retweets_tweet_id_ac1e30c4_fk_tweets_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.retweets
    ADD CONSTRAINT retweets_tweet_id_ac1e30c4_fk_tweets_id FOREIGN KEY (tweet_id) REFERENCES public.tweets(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: retweets retweets_user_id_e6648b88_fk_custom_user_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.retweets
    ADD CONSTRAINT retweets_user_id_e6648b88_fk_custom_user_id FOREIGN KEY (user_id) REFERENCES public.custom_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tweet_comment tweet_comment_comment_id_ab9de2c6_fk_comments_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.tweet_comment
    ADD CONSTRAINT tweet_comment_comment_id_ab9de2c6_fk_comments_id FOREIGN KEY (comment_id) REFERENCES public.comments(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tweet_comment tweet_comment_tweet_id_b7e029aa_fk_tweets_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.tweet_comment
    ADD CONSTRAINT tweet_comment_tweet_id_b7e029aa_fk_tweets_id FOREIGN KEY (tweet_id) REFERENCES public.tweets(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tweet_like tweet_like_like_id_611f14fd_fk_likes_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.tweet_like
    ADD CONSTRAINT tweet_like_like_id_611f14fd_fk_likes_id FOREIGN KEY (like_id) REFERENCES public.likes(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tweet_like tweet_like_tweet_id_270cb5ec_fk_tweets_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.tweet_like
    ADD CONSTRAINT tweet_like_tweet_id_270cb5ec_fk_tweets_id FOREIGN KEY (tweet_id) REFERENCES public.tweets(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tweet_tag tweet_tag_tag_id_eb4437db_fk_tags_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.tweet_tag
    ADD CONSTRAINT tweet_tag_tag_id_eb4437db_fk_tags_id FOREIGN KEY (tag_id) REFERENCES public.tags(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tweet_tag tweet_tag_tweet_id_317b1f42_fk_tweets_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.tweet_tag
    ADD CONSTRAINT tweet_tag_tweet_id_317b1f42_fk_tweets_id FOREIGN KEY (tweet_id) REFERENCES public.tweets(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tweets tweets_author_id_2519aa0a_fk_custom_user_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.tweets
    ADD CONSTRAINT tweets_author_id_2519aa0a_fk_custom_user_id FOREIGN KEY (author_id) REFERENCES public.custom_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_notifications users_notifications_notification_id_97b59280_fk_notificat; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.users_notifications
    ADD CONSTRAINT users_notifications_notification_id_97b59280_fk_notificat FOREIGN KEY (notification_id) REFERENCES public.notifications(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_notifications users_notifications_user_id_d8bb60d3_fk_custom_user_id; Type: FK CONSTRAINT; Schema: public; Owner: tw_user
--

ALTER TABLE ONLY public.users_notifications
    ADD CONSTRAINT users_notifications_user_id_d8bb60d3_fk_custom_user_id FOREIGN KEY (user_id) REFERENCES public.custom_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

