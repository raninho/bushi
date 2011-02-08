import random

from datetime import datetime
from django.test import TestCase

from encurtador.models import Link, Logger

class LinkTest(TestCase):
    def testFields(self):
        link = Link()
       
        link.key = random.choice('abcdefghijlmnopqrstuvxz')
        link.longUrl = 'http://www.sodavirtual.com.br'
        #link.date = datetime.today()
	link.save()
 
        self.assertTrue(link.id)

        logger = Logger()
	
	logger.link = link
	#logger.date = datetime.today()

	logger.save()

	self.assertTrue(logger.id)
