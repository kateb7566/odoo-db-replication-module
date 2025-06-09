# models/db_replication.py

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class DBReplicationConfig(models.Model):
    _name = "db.replication.config"
    _description = "Kateb Database Replication Configuration"

    name = fields.Char(string="Configuration Name", required=True)
    source_host = fields.Char(string="Source Host", required=True)
    source_port = fields.Integer(string="Source Port", default=5432)
    source_db = fields.Char(string="Source DB Name", required=True)
    source_user = fields.Char(string="Source User", required=True)
    source_password = fields.Char(string="Source Password", required=True)

    target_host = fields.Char(string="Target Host", required=True)
    target_port = fields.Integer(string="Target Port", default=5432)
    target_db = fields.Char(string="Target DB Name", required=True)
    target_user = fields.Char(string="Target User", required=True)
    target_password = fields.Char(string="Target Password", required=True)

    is_active = fields.Boolean(string="Is Active", default=True)
    last_synced = fields.Datetime(string="Last Synced")

    @api.model
    def sync_now(self):
        """
        Placeholder method to trigger sync logic.
        Actual implementation should handle secure and reliable data transfer.
        """
        _logger.info("Triggering sync for all active configurations.")
        active_confs = self.search([("is_active", "=", True)])
        for conf in active_confs:
            try:
                _logger.info(f"Syncing from {conf.source_db} to {conf.target_db}")
                # Call your sync logic here
                conf.last_synced = fields.Datetime.now()
            except Exception as e:
                _logger.error(f"Failed to sync config {conf.name}: {str(e)}")
