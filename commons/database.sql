create database sesp;
use sesp;


create table computers_status(
    `id` int(12) primary key auto_increment not null,
    `name` varchar(100) not null,
    `description` varchar(200)
)engine=InnoDB;


create table computers(
    `id` int(12) primary key auto_increment not null,
    `status_id` int(12) not null,
    `glpi_id` int(12)
)engine=InnoDB;


create table logs_types(
    `id` int(12) primary key auto_increment not null,
    `name` varchar(100) not null,
    `intensity` smallint not null default 1,
    `description` varchar(200)
)engine=InnoDB;
insert into `logs_types`(`name`, `intensity`, `description`) values 
('sysError', 5, 'Error in system SESP. Attention, this error not is from computer'),
('pcError', 5, 'Error in computer. Attention, this error not is from system SESP'),
('solutionFail', 4, 'System SESP failed at resolve problem'),
('glpiChangedData', 3, 'Computer data has been changed in the GLPI'),
('problemSolved', 1, 'System SESP has been solved a problem'),
('fusionNewInventory', 1, 'Computer inventory has been changed in the GLPI by FusionInventory');


create table computers_logs(
    `id` int(12) primary key auto_increment not null,
    `type_id` int(12) not null,
    `computer_id` int(12) not null,
    `when` timestamp not null default now(),
    `reference_table` varchar(100),
    `reference_id` int(12),
    `body` text
)engine=InnoDB;


create table incidents(
    `id` int(12) primary key auto_increment not null,
    `name` varchar(100) not null,
    `description` varchar(200)
)engine=InnoDB;


create table problems(
    `id` int(12) primary key auto_increment not null,
    `name` varchar(100) not null,
    `description` varchar(200)
)engine=InnoDB;


create table causes(
    `id` int(12) primary key auto_increment not null,
    `incident_id` int(12) not null,
    `problem_id` int(12) not null
)engine=InnoDB;


create table scripts_types(
    `id` int(12) primary key auto_increment not null,
    `name` varchar(100) not null,
    `description` varchar(200),
    `requirements` json
)engine=InnoDB;


create table scripts(
    `id` int(12) primary key auto_increment not null,
    `type_id` int(12) not null,
    `script` binary not null,
    `requirements` json,
    `parameters` json,
    `force_restart` boolean not null default 0,
    `force_inventory` boolean not null default 0
)engine=InnoDB;


create table solutions_types(
    `id` int(12) primary key auto_increment not null,
    `name` varchar(100) not null,
    `description` varchar(200)
)engine=InnoDB;
insert into `solutions_types`(`name`, `description`) values
('Automated', 'Script solution'),
('Manually', 'Interactive tutorial');


create table solutions(
    `id` int(12) primary key auto_increment not null,
    `name` varchar(100) not null,
    `type` int(12) not null,
    `script` int(12) not null,
    `description` varchar(200)
)engine=InnoDB;


create table to_solve(
    `id` int(12) primary key auto_increment not null,
    `problem_id` int(12) not null,
    `solution_id` int(12) not null
)engine=InnoDB;