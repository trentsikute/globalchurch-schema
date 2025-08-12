CREATE TYPE "BeliefTypeEnum" AS ENUM ('orthodox', 'roman_catholic', 'protestant', 'anglican', 'other', 'unknown');
CREATE TABLE "User" (
	user_id TEXT NOT NULL, 
	given_name TEXT, 
	family_name TEXT, 
	email TEXT, 
	telephone TEXT, 
	primary_church TEXT, 
	alternate_church TEXT, 
	interests TEXT, 
	faith_journey TEXT, 
	PRIMARY KEY (user_id)
);COMMENT ON TABLE "User" IS 'A registered platform user.';COMMENT ON COLUMN "User".user_id IS 'Unique ID for a registered platform user.';COMMENT ON COLUMN "User".given_name IS 'User’s first (given) name.';COMMENT ON COLUMN "User".family_name IS 'User’s last (family) name.';COMMENT ON COLUMN "User".email IS 'Primary contact email for the user.';COMMENT ON COLUMN "User".telephone IS 'User’s phone number (E.164).';COMMENT ON COLUMN "User".primary_church IS 'FK to the user’s primary Church.';COMMENT ON COLUMN "User".alternate_church IS 'Optional FK to a secondary/alternate Church.';COMMENT ON COLUMN "User".interests IS 'User’s interests or ministry areas.';COMMENT ON COLUMN "User".faith_journey IS 'Narrative of the user’s faith journey.';
CREATE TABLE "Church" (
	church_id TEXT NOT NULL, 
	gers_id TEXT, 
	name TEXT NOT NULL, 
	pipeline_status TEXT, 
	latitude FLOAT, 
	longitude FLOAT, 
	address TEXT, 
	locality TEXT, 
	region TEXT, 
	postal_code TEXT, 
	country TEXT NOT NULL, 
	PRIMARY KEY (church_id)
);COMMENT ON TABLE "Church" IS 'A distinct church congregation.';COMMENT ON COLUMN "Church".church_id IS 'Global.Church-issued ID for a church.';COMMENT ON COLUMN "Church".gers_id IS 'Government/Ecclesiastical Registry System identifier.';COMMENT ON COLUMN "Church".name IS 'Official church name.';COMMENT ON COLUMN "Church".pipeline_status IS 'Current enrichment pipeline stage.';COMMENT ON COLUMN "Church".latitude IS 'Latitude in decimal degrees.';COMMENT ON COLUMN "Church".longitude IS 'Longitude in decimal degrees.';COMMENT ON COLUMN "Church".address IS 'Physical street address of the church or user.';COMMENT ON COLUMN "Church".locality IS 'City or locality where the church is located.';COMMENT ON COLUMN "Church".region IS 'State, province, or administrative region.';COMMENT ON COLUMN "Church".postal_code IS 'Postal code or ZIP code for the address.';COMMENT ON COLUMN "Church".country IS 'Country code in ISO 3166-1 alpha-2 format.';
CREATE TABLE "ChurchWebsite" (
	church_id TEXT NOT NULL, 
	root_scrape_text TEXT, 
	root_scrape_buttons TEXT, 
	root_scrape_check TEXT, 
	PRIMARY KEY (church_id)
);COMMENT ON TABLE "ChurchWebsite" IS 'Raw scrape artifacts captured from the church root URL.';COMMENT ON COLUMN "ChurchWebsite".church_id IS 'Global.Church-issued ID for a church.';COMMENT ON COLUMN "ChurchWebsite".root_scrape_text IS 'Visible text content scraped from the website root page.';COMMENT ON COLUMN "ChurchWebsite".root_scrape_buttons IS 'Button texts captured on the root page.';COMMENT ON COLUMN "ChurchWebsite".root_scrape_check IS 'Checksum or status flag indicating scrape state.';
CREATE TABLE "EnrichedData" (
	church_id TEXT NOT NULL, 
	service_times TEXT, 
	church_beliefs_url TEXT, 
	trinitarian_beliefs BOOLEAN, 
	belief_type "BeliefTypeEnum", 
	scraped_email TEXT, 
	instagram_url TEXT, 
	youtube_url TEXT, 
	scraped_address TEXT, 
	church_summary TEXT, 
	PRIMARY KEY (church_id)
);COMMENT ON TABLE "EnrichedData" IS 'AI-enriched attributes extracted from the church website and socials.';COMMENT ON COLUMN "EnrichedData".church_id IS 'Global.Church-issued ID for a church.';COMMENT ON COLUMN "EnrichedData".service_times IS 'Service times for public gatherings.';COMMENT ON COLUMN "EnrichedData".church_beliefs_url IS 'URL for the church’s statement of beliefs/faith.';COMMENT ON COLUMN "EnrichedData".trinitarian_beliefs IS 'Whether the church affirms classical Trinitarian doctrine.';COMMENT ON COLUMN "EnrichedData".belief_type IS 'Denomination / church type category.
Classifies the church into a top-level Christian family as defined by BeliefTypeEnum.
Based on the Harvest Information Standards (HIS) Registry of Religions.
';COMMENT ON COLUMN "EnrichedData".scraped_email IS 'Public email address extracted from the website.';COMMENT ON COLUMN "EnrichedData".instagram_url IS 'Instagram profile URL.';COMMENT ON COLUMN "EnrichedData".youtube_url IS 'YouTube channel URL.';COMMENT ON COLUMN "EnrichedData".scraped_address IS 'Postal address extracted from the website.';COMMENT ON COLUMN "EnrichedData".church_summary IS 'Concise public summary of the church.';
CREATE TABLE "Overture" (
	id SERIAL NOT NULL, 
	gers_id TEXT, 
	version INTEGER, 
	source TEXT, 
	confidence FLOAT, 
	source_release DATE, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Overture" IS 'Original place record as supplied by Overture Maps.';COMMENT ON COLUMN "Overture".gers_id IS 'Government/Ecclesiastical Registry System identifier.';COMMENT ON COLUMN "Overture".version IS 'Overture dataset version number.';COMMENT ON COLUMN "Overture".source IS 'Source label from Overture Maps.';COMMENT ON COLUMN "Overture".confidence IS 'Confidence score (0–1) from Overture.';COMMENT ON COLUMN "Overture".source_release IS 'Overture release tag (YYYY-MM-DD).';
CREATE TABLE "User_skills" (
	"User_user_id" TEXT, 
	skills TEXT, 
	PRIMARY KEY ("User_user_id", skills), 
	FOREIGN KEY("User_user_id") REFERENCES "User" (user_id)
);COMMENT ON TABLE "User_skills" IS 'None';COMMENT ON COLUMN "User_skills"."User_user_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "User_skills".skills IS 'List of user skills.';
CREATE TABLE "ChurchWebsite_root_candidates" (
	"ChurchWebsite_church_id" TEXT, 
	root_candidates TEXT, 
	PRIMARY KEY ("ChurchWebsite_church_id", root_candidates), 
	FOREIGN KEY("ChurchWebsite_church_id") REFERENCES "ChurchWebsite" (church_id)
);COMMENT ON TABLE "ChurchWebsite_root_candidates" IS 'None';COMMENT ON COLUMN "ChurchWebsite_root_candidates"."ChurchWebsite_church_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ChurchWebsite_root_candidates".root_candidates IS 'Candidate URLs extracted from the root page.';
CREATE TABLE "ChurchWebsite_candidates_text_and_links" (
	"ChurchWebsite_church_id" TEXT, 
	candidates_text_and_links TEXT, 
	PRIMARY KEY ("ChurchWebsite_church_id", candidates_text_and_links), 
	FOREIGN KEY("ChurchWebsite_church_id") REFERENCES "ChurchWebsite" (church_id)
);COMMENT ON TABLE "ChurchWebsite_candidates_text_and_links" IS 'None';COMMENT ON COLUMN "ChurchWebsite_candidates_text_and_links"."ChurchWebsite_church_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ChurchWebsite_candidates_text_and_links".candidates_text_and_links IS 'Text snippets and associated links for candidate pages.';
CREATE TABLE "EnrichedData_service_languages" (
	"EnrichedData_church_id" TEXT, 
	service_languages TEXT, 
	PRIMARY KEY ("EnrichedData_church_id", service_languages), 
	FOREIGN KEY("EnrichedData_church_id") REFERENCES "EnrichedData" (church_id)
);COMMENT ON TABLE "EnrichedData_service_languages" IS 'None';COMMENT ON COLUMN "EnrichedData_service_languages"."EnrichedData_church_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "EnrichedData_service_languages".service_languages IS 'Languages in which services are offered.';
CREATE TABLE "EnrichedData_programs_offered" (
	"EnrichedData_church_id" TEXT, 
	programs_offered TEXT, 
	PRIMARY KEY ("EnrichedData_church_id", programs_offered), 
	FOREIGN KEY("EnrichedData_church_id") REFERENCES "EnrichedData" (church_id)
);COMMENT ON TABLE "EnrichedData_programs_offered" IS 'None';COMMENT ON COLUMN "EnrichedData_programs_offered"."EnrichedData_church_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "EnrichedData_programs_offered".programs_offered IS 'Programs or ministries the church offers.';
