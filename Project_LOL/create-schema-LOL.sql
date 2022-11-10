CREATE TABLE champion (
    c_name        varchar(20) not null,
    c_nickname    varchar(20) not null,
    c_difficulty  varchar(20)
);
CREATE TABLE skins (
    sk_champ_name  varchar(20) not null,
    sk_name        varchar(20) not null,
    sk_cost        int  not null,
    sk_skin_kind   varchar(20)
);
CREATE TABLE type (
    t_champ_name  varchar(20) not null,
    t_name        varchar(20) not null,
    t_role        varchar(20) not null
);
CREATE TABLE abilities (
    a_champ_name   varchar(20) not null,
    a_passive      varchar(45) not null,
    a_qability     varchar(45) not null,
    a_wability     varchar(45) not null,
    a_eability     varchar(45) not null,
    a_rability     varchar(45) not null
);
CREATE TABLE matchups (
    mu_champ_name   varchar(20) not null,
    bad_mu_name     varchar(20) not null,
    good_mu_name    varchar(20) not null
);
CREATE TABLE stats (
    st_champ_name   varchar(20) not null,
    st_role         varchar(2) not null,
    st_tier         char(20) not null,
    st_pickrate     int not null,
    st_matches      int not null,
    st_rank         varchar(20) not null,
    st_banrate      int not null,
    st_winrate      int not null
);