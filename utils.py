def getBestFund(w):
    "Get highest skilled fund"
    bestSkill = 0
    bestFund = None
    for f in w.funds:
        totalSkill = f.riskSkill + f.profitSkill
        if totalSkill > bestSkill:
            bestSkill = totalSkill
            bestFund = f

    return(bestFund)

def getWorstFund(w):
    "Get lowest skilled fund"
    worstSkill = 20
    worstFund = None
    for f in w.funds:
        totalSkill = f.riskSkill + f.profitSkill
        if totalSkill < worstSkill:
            worstSkill = totalSkill
            worstFund = f

    return(worstFund)

def getEstimates(f, stocks):
    "Return two lists of funds estimates for a stocks profit and risk"
    profitEstimates = []
    riskEstimates = []
    for s in stocks:
        estimate = f.estimateStock(s)
        profitEstimates.append(estimate[0])
        riskEstimates.append(estimate[1])
    return(profitEstimates, riskEstimates)
