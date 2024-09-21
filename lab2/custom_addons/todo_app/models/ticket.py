from odoo import models, fields


class Ticket(models.Model):
    _name = "todo.ticket"
    _description = "Todo Ticket"

    name = fields.Char()
    number = fields.Integer()
    tag = fields.Char()
    file = fields.Binary()
    description = fields.Text()
    state = fields.Selection([
        ('new', 'New'),
        ('doing', 'Doing'),
        ('done', 'Done')
    ], default='new')

    def action_new(self):
        print('inside action_new')
        self.state = 'new'

    def action_doing(self):
        print('inside action_doing')
        self.state = 'doing'

    def action_done(self):
        print('inside action_done')
        self.state = 'done'