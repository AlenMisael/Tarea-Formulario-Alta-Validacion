PGDMP     :    0         
    	    {            pacientesALyP    12.12    14.4                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            	           1262    60676    pacientesALyP    DATABASE     o   CREATE DATABASE "pacientesALyP" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Argentina.1252';
    DROP DATABASE "pacientesALyP";
                postgres    false            �            1259    60700 	   pacientes    TABLE     �  CREATE TABLE public.pacientes (
    id integer NOT NULL,
    dni integer,
    nombre character varying(100),
    apellido character varying(100),
    contrasenia character varying(105),
    email character varying(100),
    fecha_nacimiento date,
    telefono character varying(20),
    obra_social character varying(100),
    domicilio character varying(50),
    sexo character varying(20)
);
    DROP TABLE public.pacientes;
       public         heap    postgres    false            �            1259    60698    pacientes_id_seq    SEQUENCE     �   CREATE SEQUENCE public.pacientes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.pacientes_id_seq;
       public          postgres    false    203            
           0    0    pacientes_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.pacientes_id_seq OWNED BY public.pacientes.id;
          public          postgres    false    202            
           2604    60703    pacientes id    DEFAULT     l   ALTER TABLE ONLY public.pacientes ALTER COLUMN id SET DEFAULT nextval('public.pacientes_id_seq'::regclass);
 ;   ALTER TABLE public.pacientes ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    202    203    203                      0    60700 	   pacientes 
   TABLE DATA           �   COPY public.pacientes (id, dni, nombre, apellido, contrasenia, email, fecha_nacimiento, telefono, obra_social, domicilio, sexo) FROM stdin;
    public          postgres    false    203   7                  0    0    pacientes_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.pacientes_id_seq', 15, true);
          public          postgres    false    202            �
           2606    60710    pacientes pacientes_dni_key 
   CONSTRAINT     U   ALTER TABLE ONLY public.pacientes
    ADD CONSTRAINT pacientes_dni_key UNIQUE (dni);
 E   ALTER TABLE ONLY public.pacientes DROP CONSTRAINT pacientes_dni_key;
       public            postgres    false    203            �
           2606    60708    pacientes pacientes_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.pacientes
    ADD CONSTRAINT pacientes_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.pacientes DROP CONSTRAINT pacientes_pkey;
       public            postgres    false    203                  x������ � �     