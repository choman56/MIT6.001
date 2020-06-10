#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 08:02:24 2020

@author: Clarke Homan
"""

def findPayment(loan, r, m):
    '''
    Calculates monthly loan payment given loan amount, interest rate and number
    of months to repay    

    Args:
        loan (float): outstanding loan amount
        r (float): monthly interest rate
        m (int): months to repay

    Returns:
        monthly loan payment (with interest)

    '''
    return loan*((r*(1+r)**m)/((1+r)**m - 1))

class Mortgage(object):
    '''
    Abstract class for building different kinds of mortgages
    Creates a new mortgage of size loanm with duration of months and annual
    interest rate of annRate
    '''
    def __init__(self, loan, annRate, months):
        self.loan = loan
        self.rate = annRate/12
        self.months = months
        self.paid = [0.0]
        self.interest = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None # description of mortgage      
        
    def makePayment(self):
        '''
        Make a payment. Updates self.paid, self.outstanding and accumlated 
        self.interest amounts

        Returns:
            None.

        '''
        self.paid.append(self.payment)
        self.interest.append(self.outstanding[-1] * self.rate)
        reduction = self.payment - self.interest[-1]
        self.outstanding.append(self.outstanding[-1] - reduction)
        
    def getTotalPaid(self):
        '''
        Return the total amount paid so far

        Returns:
            Total sum pf payments

        '''
        return sum(self.paid)
    
    def getTotalInterest(self):
        '''
        Return the total interest paid over loan

        Returns:
            Total sum of interest paid

        '''
        return sum(self.interest)

    def __str__(self):
        return self.legend
    
class Fixed(Mortgage):
    def __init__(self, loan,r,months):
        '''
        Class for fixed interest mortgage no points

        Args:
            loan (float): DESCRIPTION.
            r (float): DESCRIPTION.
            months (int): DESCRIPTION.

        Returns:
            None.

        '''
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed (no points), ' + str(round(r*100, 2)) + '%'

class FixedWithPoints(Mortgage):
    def __init__(self, loan, r, months, pts):
        '''
        Class for fixed interest mortgage no points

        Args:
            loan (float): DESCRIPTION.
            r (float): DESCRIPTION.
            months (int): DESCRIPTION.
            pts (float)

        Returns:
            None.

        '''
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100)]
        self.legend = 'Fixed (with points), ' + str(round(r*100, 2)) + '%, ' + str(pts) + ' points'
    
class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserRate = teaserRate
        self.teaserMonths = teaserMonths
        self.nextRate =r/12    # interest rate after teaser period
        self.legend = 'Variable (no points) '+ str(teaserRate*100) + '% for ' + str(self.teaserMonths) + ' months, then ' + str(round(r*100, 2)) + '%'
    
    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.outstanding[-1], self.rate, self.months-self.teaserMonths)
        
        Mortgage.makePayment(self)
        
def compareMortgages(amt, years, fixedRate, pts, ptsRate, variableRate1, variableRate2, variableMonths):
    '''
    Compares the amount paid, interest paid for three types of mortgages, fixed, fixed with points and dual interest rate

    Args:
        amt (float): loan amount
        years (int): loan term
        fixedRate (float): fixed rate
        pts (float): loan points
        ptsRate (float): interest rate with points loan
        variableRate1 (float): initial (teaser) interest rate
        variableRate2 (float): residual (real) interest rate
        variableMonths (int): teaser rate term

    Returns:
        None.
        
    '''
    totalMonths = years * 12  # convert term years to term months
    
    fixedLoan = Fixed(amt, fixedRate, totalMonths) # create fixed mortgage
    
    fixedWithPtsLoan = FixedWithPoints(amt, ptsRate, totalMonths, pts) # create fixed with points mortgage
    
    variableRateLoan = TwoRate(amt, variableRate2, totalMonths, variableRate1, variableMonths)
    
    mortgagesList = [fixedLoan, fixedWithPtsLoan, variableRateLoan]
    
    for monthNum in range(totalMonths):
        for mortgage in mortgagesList:
            mortgage.makePayment()
            
    for mortgage in mortgagesList:
        print('\n',mortgage)
        print('Total payment is: $' + str(int(mortgage.getTotalPaid())))
        print('Total interest is: $' + str(int(mortgage.getTotalInterest())))


loanAmount = int(input('Enter loan amount: '))
term = int(input('Enter loan term in years: '))

compareMortgages(amt=loanAmount, years=term, fixedRate=0.07, pts=3.25, 
                  ptsRate=0.05, variableRate1=0.045, 
                  variableRate2=0.095, variableMonths=48)
    
    