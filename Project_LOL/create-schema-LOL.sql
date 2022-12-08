CREATE TABLE champion (
    c_key         int not null,
    c_name        varchar(20) not null,
    c_nickname    varchar(20) not null,
    c_difficulty  varchar(20),
    PRIMARY KEY (c_key)
);
CREATE TABLE skins (
    sk_key         int not null,
    sk_champ_name  varchar(20) not null,
    sk_name        varchar(20) not null,
    sk_cost        int  not null,
    sk_skin_kind   varchar(20),
    PRIMARY KEY (sk_key)
);
CREATE TABLE type (
    t_key         int not null,
    t_champ_name  varchar(20) not null,
    t_name        varchar(20) not null,
    t_role        varchar(20) not null,
    PRIMARY KEY (t_key)
);
CREATE TABLE abilities (
    a_key          int not null,
    a_champ_name   varchar(20) not null,
    a_passive      varchar(45) not null,
    a_qability     varchar(45) not null,
    a_wability     varchar(45) not null,
    a_eability     varchar(45) not null,
    a_rability     varchar(45) not null,
    PRIMARY KEY (a_key)
);
CREATE TABLE matchups (
    mu_key          int not null,
    mu_champ_name   varchar(20) not null,
    bad_mu_name     varchar(20) not null,
    good_mu_name    varchar(20) not null,
    PRIMARY KEY (mu_key)
);
CREATE TABLE stats (
    st_key          int not null,
    st_champ_name   varchar(20) not null,
    st_role         varchar(2) not null,
    st_tier         char(20) not null,
    st_pickrate     int not null,
    st_matches      int not null,
    st_rank         varchar(20) not null,
    st_banrate      int not null,
    st_winrate      int not null,
    PRIMARY KEY (st_key)
);