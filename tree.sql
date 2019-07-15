--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: users; Type: TABLE; Schema: public; Owner: tongyifan; Tablespace: 
--

CREATE TABLE users (
    uid integer NOT NULL,
    username character varying(40) NOT NULL,
    privacy integer DEFAULT 0 NOT NULL,
    alive integer DEFAULT 1 NOT NULL,
    master integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.users OWNER TO tongyifan;

--
-- Name: users_pk; Type: CONSTRAINT; Schema: public; Owner: tongyifan; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pk PRIMARY KEY (uid);


--
-- Name: users_uid_uindex; Type: INDEX; Schema: public; Owner: tongyifan; Tablespace: 
--

CREATE UNIQUE INDEX users_uid_uindex ON users USING btree (uid);


--
-- Name: users_username_uindex; Type: INDEX; Schema: public; Owner: tongyifan; Tablespace: 
--

CREATE UNIQUE INDEX users_username_uindex ON users USING btree (username);


--
-- PostgreSQL database dump complete
--