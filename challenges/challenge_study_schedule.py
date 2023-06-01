def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    estudantes_online = 0
    for horario_inicio, horario_saida in permanence_period:
        if not isinstance(horario_inicio, int) \
                or not isinstance(horario_saida, int):
            return None
        if horario_inicio <= target_time <= horario_saida:
            estudantes_online += 1
    return estudantes_online


# Teste do Requisito
# permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# print(study_schedule(permanence_periods, 1))
