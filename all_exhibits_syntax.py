exhibit_stakeholders = {
    # 2: dict(students="""CROSSTABS
    #                     /TABLES=Finished BY Grade_Level
    #                     /FORMAT=AVALUE TABLES
    #                     /CELLS=COUNT
    #                     /COUNT ROUND CELL.
    #                 """,
    #         parents="""FREQUENCIES VARIABLES= Finished
    #                     /ORDER=ANALYSIS.
    #                 """,
    #         staff="""FREQUENCIES VARIABLES= Finished
    #                 /ORDER=ANALYSIS."""),
    # 3: dict(parents="""FREQUENCIES VARIABLES=Parent_Hebrew_Proficiency
    #                 /ORDER=ANALYSIS."""),
    # 4: dict(students="""FREQUENCIES VARIABLES= Attend_Overnight_Camp_Yes_No
    #                 Attend_Youth_Group_Yes_No
    #                 Visited_Israel_TwicePlus_Yes_No
    #                 Attend_Synagoge_Often_Yes_No
    #                 /ORDER=ANALYSIS.""",
    #         parents="""FREQUENCIES VARIABLES=Day_School_Experience
    #                 /ORDER=ANALYSIS."""),
    # 5: dict(students="""FREQUENCIES VARIABLES= Important_learn_hebrew_communication
    #                 /ORDER=ANALYSIS.""",
    #         parents="""FREQUENCIES VARIABLES= Important_learn_hebrew_communication
    #                 /ORDER=ANALYSIS.""",
    #         staff="""FREQUENCIES VARIABLES= Important_forstaff_hebrewforcommunication
    #                  /ORDER=ANALYSIS."""),
    # 6: dict(students="""CTABLES
    #                     /VLABELS VARIABLES=
    #                     A_D_important_hebrew_connects_jewsYes_No
    #                     A_D_important_hebrew_part_group_mix_hebrewYes_No
    #                     A_D_important_hebrew_part_being_jewishYes_No
    #                     A_D_important_hebrew_maintains_jewish_languageYes_No
    #                     A_D_important_hebrew_connect_israelYes_No
    #                     A_D_important_hebrew_prepares_aliyaYes_No
    #                     A_D_important_hebrew_helps_visit_israelYes_No
    #                     A_D_important_hebrew_read_modern_israel_booksYes_No
    #                     A_D_important_hebrew_communicate_jews_worldYes_No
    #                     A_D_important_hebrew_communicate_hebrew_speakersYes_No
    #                     A_D_important_hebrew_learn_2ndlanguageYes_No
    #                     DISPLAY=LABEL
    #                     /TABLE
    #                     A_D_important_hebrew_connects_jewsYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_part_group_mix_hebrewYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_part_being_jewishYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_maintains_jewish_languageYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_connect_israelYes_No  [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_prepares_aliyaYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_helps_visit_israelYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_read_modern_israel_booksYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_communicate_jews_worldYes_No   [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_communicate_hebrew_speakersYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_learn_2ndlanguageYes_No [C][COLPCT.COUNT PCT40.1]
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_connects_jewsYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_part_group_mix_hebrewYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrew_part_being_jewishYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_maintains_jewish_languageYes_No  [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrew_connect_israelYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_prepares_aliyaYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_helps_visit_israelYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_read_modern_israel_booksYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrew_communicate_jews_worldYes_No  [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_communicate_hebrew_speakersYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_learn_2ndlanguageYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /TITLES
    #                     TITLE='*Exhibit 6: Why is Heb for comm important.'.""",
    #         parents="""CTABLES
    #                     /VLABELS VARIABLES=
    #                     A_D_important_hebrew_connects_jewsYes_No
    #                     A_D_important_hebrew_part_group_mix_hebrewYes_No
    #                     A_D_important_hebrew_part_being_jewishYes_No
    #                     A_D_important_hebrew_maintains_jewish_languageYes_No
    #                     A_D_important_hebrew_connect_israelYes_No
    #                     A_D_important_hebrew_prepares_aliyaYes_No
    #                     A_D_important_hebrew_helps_visit_israelYes_No
    #                     A_D_important_hebrew_read_modern_israel_booksYes_No
    #                     A_D_important_hebrew_communicate_jews_worldYes_No
    #                     A_D_important_hebrew_communicate_hebrew_speakersYes_No
    #                     A_D_important_hebrew_learn_2ndlanguageYes_No
    #                     DISPLAY=LABEL
    #                     /TABLE
    #                     A_D_important_hebrew_connects_jewsYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_part_group_mix_hebrewYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_part_being_jewishYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_maintains_jewish_languageYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_connect_israelYes_No  [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_prepares_aliyaYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_helps_visit_israelYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_read_modern_israel_booksYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_communicate_jews_worldYes_No   [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_communicate_hebrew_speakersYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrew_learn_2ndlanguageYes_No [C][COLPCT.COUNT PCT40.1]
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_connects_jewsYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_part_group_mix_hebrewYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrew_part_being_jewishYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_maintains_jewish_languageYes_No  [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrew_connect_israelYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_prepares_aliyaYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_helps_visit_israelYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_read_modern_israel_booksYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrew_communicate_jews_worldYes_No  [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_communicate_hebrew_speakersYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES= A_D_important_hebrew_learn_2ndlanguageYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /TITLES
    #                     TITLE='*Exhibit 6: Why is Heb for comm important.'.""",
    #         staff="""CTABLES
    #                 /VLABELS VARIABLES=
    #                 A_D_important_hebrew_connects_jewsYes_No
    #                 A_D_important_hebrew_part_group_mix_hebrewYes_No
    #                 A_D_important_hebrew_part_being_jewishYes_No
    #                 A_D_important_hebrew_maintains_jewish_languageYes_No
    #                 A_D_important_hebrew_connect_israelYes_No
    #                 A_D_important_hebrew_prepares_aliyaYes_No
    #                 A_D_important_hebrew_helps_visit_israelYes_No
    #                 A_D_important_hebrew_read_modern_israel_booksYes_No
    #                 A_D_important_hebrew_communicate_jews_worldYes_No
    #                 A_D_important_hebrew_communicate_hebrew_speakersYes_No
    #                 A_D_important_hebrew_learn_2ndlanguageYes_No
    #                 DISPLAY=LABEL
    #                 /TABLE
    #                 A_D_important_hebrew_connects_jewsYes_No [C][COLPCT.COUNT PCT40.1] +
    #                 A_D_important_hebrew_part_group_mix_hebrewYes_No [C][COLPCT.COUNT PCT40.1] +
    #                 A_D_important_hebrew_part_being_jewishYes_No [C][COLPCT.COUNT PCT40.1] +
    #                 A_D_important_hebrew_maintains_jewish_languageYes_No [C][COLPCT.COUNT PCT40.1] +
    #                 A_D_important_hebrew_connect_israelYes_No  [C][COLPCT.COUNT PCT40.1] +
    #                 A_D_important_hebrew_prepares_aliyaYes_No [C][COLPCT.COUNT PCT40.1] +
    #                 A_D_important_hebrew_helps_visit_israelYes_No [C][COLPCT.COUNT PCT40.1] +
    #                 A_D_important_hebrew_read_modern_israel_booksYes_No [C][COLPCT.COUNT PCT40.1] +
    #                 A_D_important_hebrew_communicate_jews_worldYes_No   [C][COLPCT.COUNT PCT40.1] +
    #                 A_D_important_hebrew_communicate_hebrew_speakersYes_No [C][COLPCT.COUNT PCT40.1] +
    #                 A_D_important_hebrew_learn_2ndlanguageYes_No [C][COLPCT.COUNT PCT40.1]
    #                 /CATEGORIES VARIABLES= A_D_important_hebrew_connects_jewsYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES= A_D_important_hebrew_part_group_mix_hebrewYes_No [0, 1, OTHERNM]
    #                 EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES=A_D_important_hebrew_part_being_jewishYes_No [0, 1, OTHERNM]
    #                 EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES= A_D_important_hebrew_maintains_jewish_languageYes_No  [0, 1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES=A_D_important_hebrew_connect_israelYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES= A_D_important_hebrew_prepares_aliyaYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES= A_D_important_hebrew_helps_visit_israelYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES= A_D_important_hebrew_read_modern_israel_booksYes_No [0, 1, OTHERNM]
    #                 EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES=A_D_important_hebrew_communicate_jews_worldYes_No  [0, 1, OTHERNM]
    #                 EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES= A_D_important_hebrew_communicate_hebrew_speakersYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES= A_D_important_hebrew_learn_2ndlanguageYes_No [0, 1, OTHERNM]
    #                 EMPTY=INCLUDE
    #                 /TITLES
    #                 TITLE='*Exhibit 6: Why is Heb for comm important.'."""),
    # 7: dict(parents="""FREQUENCIES VARIABLES=Satisfied_instruction_hebrewforcommunication
    #                 /ORDER=ANALYSIS.""",
    #         staff="""FREQUENCIES VARIABLES=Satisfied_instruction_hebrewforcommunication
    #                 /ORDER=ANALYSIS."""),
    # 8: dict(parents="""MULT RESPONSE GROUPS=$Challanges.Heb.comm (
    #                 challanges_conversational_teacherexpertise
    #                 challanges_conversational_teachers_lowknowledge
    #                 challanges_conversational_curriculum_bad
    #                 challanges_conversational_instruction_english
    #                 challanges_conversational_teachers_dontcare
    #                 challanges_conversational_not_priority
    #                 challanges_conversational_lackoftime
    #                 challanges_conversational_diversity_hebrewlevels
    #                 challanges_conversational_number_child_classes
    #                 challanges_conversational_firstclass_canceled (1))
    #                 /FREQUENCIES=$Challanges.Heb.comm.""",
    #         staff="""MULT RESPONSE GROUPS=$Challanges.Heb.comm (
    #                 Hard_produce_highlevels_hebforcom_teacherexpertise
    #                 Hard_produce_highlevels_hebforcom_teachers_lowknowledge
    #                 Hard_produce_highlevels_hebforcom_curriculum_bad
    #                 Hard_produce_highlevels_hebforcom_instruction_english
    #                 Hard_produce_highlevels_hebforcom_teachers_dontcare
    #                 Hard_produce_highlevels_hebforcom_not_priority
    #                 Hard_produce_highlevels_hebforcom_lackoftime
    #                 Hard_produce_highlevels_hebforcom_diversity_hebrewlevels
    #                 Hard_produce_highlevels_hebforcom_number_child_classes
    #                 Hard_produce_highlevels_hebforcom_firstclass_canceled (1))
    #                 /FREQUENCIES=$Challanges.Heb.comm."""),
    # 9: dict(staff="""CTABLES
    #                 /VLABELS VARIABLES=
    #                 Support_available_prof_development
    #                 Support_available_time
    #                 Support_available_admin_support
    #                 Support_available_hebforcom_assesments_instrument
    #                 Support_available_classroom_support
    #                 Support_available_hebforcom_curriculum
    #                 Support_available_resources_specialneeds_gifted
    #                 Support_available_hebfortext_assesments_instrument
    #                 Support_available_hebfortext_curriculum
    #                 Support_available_pedogogical_material
    #                 DISPLAY=LABEL
    #                 /TABLE
    #                 Support_available_prof_development [C][COLPCT.COUNT PCT40.1] +
    #                 Support_available_time [C][COLPCT.COUNT PCT40.1] +
    #                 Support_available_admin_support [C][COLPCT.COUNT PCT40.1] +
    #                 Support_available_hebforcom_assesments_instrument [C][COLPCT.COUNT PCT40.1] +
    #                 Support_available_classroom_support [C][COLPCT.COUNT PCT40.1] +
    #                 Support_available_hebforcom_curriculum [C][COLPCT.COUNT PCT40.1] +
    #                 Support_available_resources_specialneeds_gifted [C][COLPCT.COUNT PCT40.1] +
    #                 Support_available_hebfortext_assesments_instrument [C][COLPCT.COUNT PCT40.1] +
    #                 Support_available_hebfortext_curriculum [C][COLPCT.COUNT PCT40.1] +
    #                 Support_available_pedogogical_material  [C][COLPCT.COUNT PCT40.1]
    #                 /CATEGORIES VARIABLES=Support_available_prof_development  [1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES=Support_available_time [1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES=Support_available_admin_support [1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES=Support_available_hebforcom_assesments_instrument [1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES=Support_available_classroom_support [1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES=Support_available_hebforcom_curriculum [1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES=Support_available_resources_specialneeds_gifted [1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES=Support_available_hebfortext_assesments_instrument [1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES=Support_available_hebfortext_curriculum [1, OTHERNM] EMPTY=INCLUDE
    #                 /CATEGORIES VARIABLES=Support_available_pedogogical_material [1, OTHERNM] EMPTY=INCLUDE
    #                 /TITLES
    #                 TITLE='*Exhibit 9: Staff Report of Availability of School Resources.'."""),
    # 10: dict(parents="""Frequencies variables=Comapred_personal_experience_rate_Hebrew
    #         Comapred_personal_experience_rate_Hebrew_explain
    #         /order=analysis."""),
    # 11: dict(students="""Frequencies variables=A_D_teaching_hebrewforcommunication_fun_interesting
    #                     A_D_like_learning_materials_hebrewclasses
    #                     /order=analysis."""),
    # 12: dict(students="""Frequencies variables=
    #         Compared_othertopics_rate_hebrew
    #         Compared_secondlanguageclasses_doing_hebrewforcommunication
    #         /order=analysis."""),
    # 13: dict(students="""Frequencies variables=
    #         Feelings_hebrew_at_school_hebrewforcommunication
    #         /order=analysis."""),
    # 14: dict(students="""CTABLES
    #                     /VLABELS VARIABLES=Rate_current_hebrew_level_reading_hebrewforcommunication
    #                     Rate_current_hebrew_level_writing_hebrewforcommunication
    #                     Rate_current_hebrew_level_speaking_hebrewforcommunication
    #                     Rate_current_hebrew_level_understanding_hebrewforcommunication Grade_Level DISPLAY=LABEL
    #                     /TABLE Rate_current_hebrew_level_reading_hebrewforcommunication [S][MEAN] +
    #                     Rate_current_hebrew_level_writing_hebrewforcommunication [S][MEAN] +
    #                     Rate_current_hebrew_level_speaking_hebrewforcommunication [S][MEAN] +
    #                     Rate_current_hebrew_level_understanding_hebrewforcommunication [S][MEAN] BY Grade_Level [C]
    #                     /CATEGORIES VARIABLES=Grade_Level ORDER=A KEY=VALUE EMPTY=INCLUDE
    #                     /CRITERIA CILEVEL=95
    #                     /TITLES
    #                     TITLE='*Exhibit 14: Stakeholders Perceptions of Hebrew Domains.'.""",
    #          parents="""CTABLES
    #                     /VLABELS VARIABLES=Rate_current_hebrew_level_reading_hebrewforcommunication
    #                     Rate_current_hebrew_level_writing_hebrewforcommunication
    #                     Rate_current_hebrew_level_speaking_hebrewforcommunication
    #                     Rate_current_hebrew_level_understanding_hebrewforcommunication DISPLAY=LABEL
    #                     /TABLE Rate_current_hebrew_level_reading_hebrewforcommunication [S][MEAN] +
    #                     Rate_current_hebrew_level_writing_hebrewforcommunication [S][MEAN] +
    #                     Rate_current_hebrew_level_speaking_hebrewforcommunication [S][MEAN] +
    #                     Rate_current_hebrew_level_understanding_hebrewforcommunication [S][MEAN]
    #                     /TITLES
    #                     TITLE='*Exhibit 14: Stakeholders Perceptions of Hebrew Domains.'.""",
    #          staff="""CTABLES
    #                     /VLABELS VARIABLES=Rate_current_hebrew_level_reading_hebrewforcommunication
    #                     Rate_current_hebrew_level_writing_hebrewforcommunication
    #                     Rate_current_hebrew_level_speaking_hebrewforcommunication
    #                     Rate_current_hebrew_level_understanding_hebrewforcommunication DISPLAY=LABEL
    #                     /TABLE Rate_current_hebrew_level_reading_hebrewforcommunication [S][MEAN] +
    #                     Rate_current_hebrew_level_writing_hebrewforcommunication [S][MEAN] +
    #                     Rate_current_hebrew_level_speaking_hebrewforcommunication [S][MEAN] +
    #                     Rate_current_hebrew_level_understanding_hebrewforcommunication [S][MEAN]
    #                     /TITLES
    #                     TITLE='*Exhibit 14: Stakeholders Perceptions of Hebrew Domains.'."""),
    # 15: dict(students="""CTABLES
    #                     /VLABELS VARIABLES=A_D_chat_in_hebrew A_D_speak_hebrew_class A_D_understand_israeli_songs
    #                     A_D_understand_israelinews_literature A_D_understand_hebrew_socialmedia
    #                     A_D_understand_teachers_speakhebrew Grade_Level
    #                     DISPLAY=LABEL
    #                     /TABLE A_D_chat_in_hebrew [C] + A_D_speak_hebrew_class [C] + A_D_understand_israeli_songs [C] +
    #                     A_D_understand_israelinews_literature [C] + A_D_understand_hebrew_socialmedia [C] +
    #                     A_D_understand_teachers_speakhebrew [C] BY Grade_Level [C][COLPCT.COUNT PCT40.1]
    #                     /CATEGORIES VARIABLES=A_D_chat_in_hebrew A_D_speak_hebrew_class A_D_understand_israeli_songs
    #                     A_D_understand_israelinews_literature A_D_understand_hebrew_socialmedia
    #                     A_D_understand_teachers_speakhebrew Grade_Level ORDER=A KEY=VALUE EMPTY=INCLUDE MISSING=EXCLUDE
    #                     /CRITERIA CILEVEL=95
    #                     /TITLES
    #                     TITLE=' Exhibit 15: Students Assessment of their Hebrew Communication Abilities.'."""),
    # 16: dict(students="""FREQUENCIES VARIABLES= Important_learn_hebrew_textstudy
    #                     /ORDER=ANALYSIS.""",
    #          parents="""FREQUENCIES VARIABLES= Important_learn_hebrew_textstudy
    #                     /ORDER=ANALYSIS.""",
    #          staff="""FREQUENCIES VARIABLES= Important_forstaff_hebrewfortext
    #                     /ORDER=ANALYSIS."""),
    # 17: dict(students="""CTABLES
    #                     /VLABELS VARIABLES=
    #                     A_D_important_hebrewtext_jewish_hertiageYes_No
    #                     A_D_important_hebrewtext_prepares_leadprayersYes_No
    #                     A_D_important_hebrewtext_comfortable_servicesYes_No
    #                     A_D_important_hebrewtext_appreciation_jewish_cultureYes_No
    #                     A_D_important_hebrewtext_feel_part_synagogueYes_No
    #                     A_D_important_hebrewtext_deepens_understanding_textYes_No
    #                     A_D_important_hebrewtext_understand_text_original_languageYes_No
    #                     A_D_important_hebrewtext_read_outlouad_textYes_No
    #                     A_D_important_hebrewtext_understanding_prayersYes_No
    #                     A_D_important_hebrewtext_prepares_studying_text_Yes_No
    #                     DISPLAY=LABEL
    #                     /TABLE
    #                     A_D_important_hebrewtext_jewish_hertiageYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_prepares_leadprayersYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_comfortable_servicesYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_appreciation_jewish_cultureYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_feel_part_synagogueYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_deepens_understanding_textYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_understand_text_original_languageYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_read_outlouad_textYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_understanding_prayersYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_prepares_studying_text_Yes_No [C][COLPCT.COUNT PCT40.1]
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_jewish_hertiageYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_prepares_leadprayersYes_No  [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_comfortable_servicesYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_appreciation_jewish_cultureYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_feel_part_synagogueYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_deepens_understanding_textYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_understand_text_original_languageYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_read_outlouad_textYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_understanding_prayersYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_prepares_studying_text_Yes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /TITLES
    #                     TITLE=' Exhibit 17: Why is Heb for text study important.'.""",
    #          parents="""CTABLES
    #                     /VLABELS VARIABLES=
    #                     A_D_important_hebrewtext_jewish_hertiageYes_No
    #                     A_D_important_hebrewtext_prepares_leadprayersYes_No
    #                     A_D_important_hebrewtext_comfortable_servicesYes_No
    #                     A_D_important_hebrewtext_appreciation_jewish_cultureYes_No
    #                     A_D_important_hebrewtext_feel_part_synagogueYes_No
    #                     A_D_important_hebrewtext_deepens_understanding_textYes_No
    #                     A_D_important_hebrewtext_understand_text_original_languageYes_No
    #                     A_D_important_hebrewtext_read_outlouad_textYes_No
    #                     A_D_important_hebrewtext_understanding_prayersYes_No
    #                     A_D_important_hebrewtext_prepares_studying_text_Yes_No
    #                     DISPLAY=LABEL
    #                     /TABLE
    #                     A_D_important_hebrewtext_jewish_hertiageYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_prepares_leadprayersYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_comfortable_servicesYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_appreciation_jewish_cultureYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_feel_part_synagogueYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_deepens_understanding_textYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_understand_text_original_languageYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_read_outlouad_textYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_understanding_prayersYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_prepares_studying_text_Yes_No [C][COLPCT.COUNT PCT40.1]
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_jewish_hertiageYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_prepares_leadprayersYes_No  [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_comfortable_servicesYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_appreciation_jewish_cultureYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_feel_part_synagogueYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_deepens_understanding_textYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_understand_text_original_languageYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_read_outlouad_textYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_understanding_prayersYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_prepares_studying_text_Yes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /TITLES
    #                     TITLE=' Exhibit 17: Why is Heb for text study important.'.""",
    #          staff="""CTABLES
    #                     /VLABELS VARIABLES=
    #                     A_D_important_hebrewtext_jewish_hertiageYes_No
    #                     A_D_important_hebrewtext_prepares_leadprayersYes_No
    #                     A_D_important_hebrewtext_comfortable_servicesYes_No
    #                     A_D_important_hebrewtext_appreciation_jewish_cultureYes_No
    #                     A_D_important_hebrewtext_feel_part_synagogueYes_No
    #                     A_D_important_hebrewtext_deepens_understanding_textYes_No
    #                     A_D_important_hebrewtext_understand_text_original_languageYes_No
    #                     A_D_important_hebrewtext_read_outlouad_textYes_No
    #                     A_D_important_hebrewtext_understanding_prayersYes_No
    #                     A_D_important_hebrewtext_prepares_studying_text_Yes_No
    #                     DISPLAY=LABEL
    #                     /TABLE
    #                     A_D_important_hebrewtext_jewish_hertiageYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_prepares_leadprayersYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_comfortable_servicesYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_appreciation_jewish_cultureYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_feel_part_synagogueYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_deepens_understanding_textYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_understand_text_original_languageYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_read_outlouad_textYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_understanding_prayersYes_No [C][COLPCT.COUNT PCT40.1] +
    #                     A_D_important_hebrewtext_prepares_studying_text_Yes_No [C][COLPCT.COUNT PCT40.1]
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_jewish_hertiageYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_prepares_leadprayersYes_No  [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_comfortable_servicesYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_appreciation_jewish_cultureYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_feel_part_synagogueYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_deepens_understanding_textYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_understand_text_original_languageYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_read_outlouad_textYes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_understanding_prayersYes_No [0, 1, OTHERNM] EMPTY=INCLUDE
    #                     /CATEGORIES VARIABLES=A_D_important_hebrewtext_prepares_studying_text_Yes_No [0, 1, OTHERNM]
    #                     EMPTY=INCLUDE
    #                     /TITLES
    #                     TITLE=' Exhibit 17: Why is Heb for text study important.'."""),
    # 18: dict(parents="""FREQUENCIES VARIABLES=
    #                     Satisfied_instruction_hebrewfortext
    #                     /ORDER=ANALYSIS.""",
    #          staff="""FREQUENCIES VARIABLES=
    #                     Satisfied_instruction_hebrewfortext
    #                     /ORDER=ANALYSIS."""),
    # 19: dict(parents="""MULT RESPONSE GROUPS=$Challanges.Heb.text (
    #                     challanges_hebrew_text_study_teacher_inexperienced
    #                     challanges_hebrew_text_study_lowknowledge
    #                     challanges_hebrew_text_study_instruction_english
    #                     challanges_hebrew_text_study_nopriority_masterclassics
    #                     challanges_hebrew_text_study_notenough_textteachers
    #                     challanges_hebrew_text_study_notenoughtime
    #                     challanges_hebrew_text_study_texts_taughtintranslation
    #                     challanges_hebrew_text_study_number_child_classes
    #                     challanges_hebrew_text_study_conducted_ivritbivrit
    #                     challanges_hebrew_text_study_diversity_hebrewlevels (1))
    #                     /FREQUENCIES=$Challanges.Heb.text.""",
    #          staff="""MULT RESPONSE GROUPS=$Challanges.Heb.text (
    #                     Hard_produce_highlevels_hebfortext_teacher_inexperienced
    #                     Hard_produce_highlevels_hebfortext_lowknowledge
    #                     Hard_produce_highlevels_hebfortext_instruction_english
    #                     Hard_produce_highlevels_hebfortext_nopriority_masterclassics
    #                     Hard_produce_highlevels_hebfortext_notenough_textteachers
    #                     Hard_produce_highlevels_hebfortext_notenoughtime
    #                     Hard_produce_highlevels_hebfortext_texts_taughtintranslation
    #                     Hard_produce_highlevels_hebfortext_number_child_classes
    #                     Hard_produce_highlevels_hebfortext_conducted_ivritbivrit
    #                     Hard_produce_highlevels_hebfortext_diversity_hebrewlevels (1))
    #                     /FREQUENCIES=$Challanges.Heb.text."""),
    # 20: dict(students="""Frequencies variables=
    #                     Feelings_hebrew_at_school_hebrewfortext
    #                     /order=analysis."""),
    # 21: dict(students="""CTABLES
    #                     /VLABELS VARIABLES=Rate_current_hebrew_level_reading_hebrewfortext
    #                     Rate_current_hebrew_level_understanding_hebrewfortext Grade_Level DISPLAY=LABEL
    #                     /TABLE Rate_current_hebrew_level_reading_hebrewfortext [S][MEAN] +
    #                     Rate_current_hebrew_level_understanding_hebrewfortext [S][MEAN]  BY Grade_Level [C]
    #                     /CATEGORIES VARIABLES=Grade_Level ORDER=A KEY=VALUE EMPTY=INCLUDE
    #                     /CRITERIA CILEVEL=95
    #                     /TITLES
    #                     TITLE='Exhibit 21: Stakeholders Perceptions of Hebrew for text study.'.""",
    #          parents="""CTABLES
    #                     /VLABELS VARIABLES=Rate_current_hebrew_level_reading_hebrewfortext
    #                     Rate_current_hebrew_level_understanding_hebrewfortext DISPLAY=LABEL
    #                     /TABLE Rate_current_hebrew_level_reading_hebrewfortext [S][MEAN] +
    #                     Rate_current_hebrew_level_understanding_hebrewfortext [S][MEAN]
    #                     /TITLES
    #                     TITLE='Exhibit 21: Stakeholders Perceptions of Hebrew for text study.'.""",
    #          staff="""CTABLES
    #                 /VLABELS VARIABLES=Rate_current_hebrew_level_reading_hebrewfortext
    #                 Rate_current_hebrew_level_understanding_hebrewfortext DISPLAY=LABEL
    #                 /TABLE Rate_current_hebrew_level_reading_hebrewfortext [S][MEAN] +
    #                 Rate_current_hebrew_level_understanding_hebrewfortext [S][MEAN]
    #                 /TITLES
    #                 TITLE='*Exhibit 21: Stakeholders Perceptions of Hebrew for text study.'."""),
    22: dict(students="""CTABLES
                        /VLABELS VARIABLES=A_D_read_unfamiliar_siddurtext
                        A_D_understand_familiar_siddurtext
                        A_D_lead_prayer
                        A_D_chant_torah
                        A_D_learn_jewish_text_independently
                        DISPLAY=LABEL
                        /TABLE A_D_read_unfamiliar_siddurtext [C] +
                        A_D_understand_familiar_siddurtext [C] +
                        A_D_lead_prayer [C] +
                        A_D_chant_torah [C] +
                        A_D_learn_jewish_text_independently[C]  BY Grade_Level [C][COLPCT.COUNT PCT40.1]
                        /CATEGORIES VARIABLES=A_D_read_unfamiliar_siddurtext
                        A_D_understand_familiar_siddurtext
                        A_D_lead_prayer
                        A_D_chant_torah
                        A_D_learn_jewish_text_independently Grade_Level ORDER=A KEY=VALUE EMPTY=INCLUDE MISSING=EXCLUDE
                        /CRITERIA CILEVEL=95
                        /TITLES
                        TITLE=' Exhibit 22: Students Assessment of their Hebrew for Text Study and Prayer Abilities.'.""")
}