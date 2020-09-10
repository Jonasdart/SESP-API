create database sesp;
use sesp;


create table computers_status(
    `id` int(12) primary key auto_increment not null,
    `name` varchar(100) not null,
    `description` varchar(200)
)engine=InnoDB;
insert into `computers_status`(`name`,`description`) values
('Nome fora do padrao', 'Aguardando alteração de nome'),
('Fusion indisponível', 'Aguardando instalação do Fusion Inventory'),
('Fusion server inacessível', 'O servidor http do Fusion Inventory utilizado para forçar o inventário não está acessível'),
('Inconsistência de IP', 'A informação de IP da requisição não bate com a informação de IP do GLPI'),
('Em erro', 'o SESP encontrou erros que não foram resolvidos'),
('Aguardando', 'Aguardando triagem de status'),
('Pronto', 'Aguardando o próximo inventário do Fusion');


create table computers(
    `computer_id` int(12) primary key auto_increment not null,
    `computer_name` varchar(100) not null,
    `inventory_number` varchar(100),
    `status_id` int(12) not null,
    `last_request_host` varchar(100) not null,
    `next_fusion_inventory` varchar(100),
    `next_reboot` varchar(100),
    `next_shutdown` varchar(100),
    `glpi_id` int(12),
    `glpi_name` varchar(100),
    unique(computer_name)
)engine=InnoDB;

create table logs_types(
    `id` int(12) primary key auto_increment not null,
    `name` varchar(100) not null,
    `intensity` smallint not null default 1,
    `description` varchar(200)
)engine=InnoDB;
insert into `logs_types`(`name`, `intensity`, `description`) values 
('apiError', 5, 'Error in API service.'),
('sysError', 5, 'Error in system SESP. Attention, this error not is from computer'),
('pcError', 5, 'Error in computer. Attention, this error not is from system SESP'),
('pcAlert', 4, 'Computer info . Computer information does not match GLPI information'),
('solutionFail', 4, 'System SESP failed at resolve problem'),
('glpiChangedData', 3, 'Computer data has been changed in the GLPI'),
('problemSolved', 1, 'System SESP has been solved a problem'),
('fusionNewInventory', 1, 'Computer inventory has been changed in the GLPI by FusionInventory');


create table api_logs(
    `id` int(12) primary key auto_increment not null,
    `type_id` int(12) not null,
    `route` varchar(100),
    `method` varchar(100),
    `applicant` varchar(100),
    `when` timestamp not null default now(),
    `body` text
)engine=InnoDB;


create table computers_logs(
    `id` int(12) primary key auto_increment not null,
    `type_id` int(12) not null,
    `computer_id` int(12),
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