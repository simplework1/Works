CREATE TABLE public.roles (
    id UUID PRIMARY KEY,
    name VARCHAR(255),
    userfetch BOOLEAN,
    username VARCHAR(255),
    taskweek BOOLEAN,
    taskplan BOOLEAN,
    taskimport BOOLEAN,
    searchhistory BOOLEAN,
    search BOOLEAN,
    taskselect BOOLEAN,
    taskedit BOOLEAN
);
