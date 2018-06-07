import grpc
from common.protobuf.com import auditor_pb2, auditor_pb2_grpc
from common.protobuf.com import com_pb2

MAX_MESSAGE_LENGTH = 4 * 1024 * 1024 * 10
options = [
    ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
    ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)
]

channel = grpc.insecure_channel(
    '10.128.0.89:50049',
    options=options,
)

stub = auditor_pb2_grpc.AuditorServiceStub(channel)

# creating new application
application = auditor_pb2.Application(
	name="stpos_test",
	environment="staging"
)

stub.CreateApplication(application)
# id is 2


# getting the application id
application = auditor_pb2.Application(
	name="stpos_test",
	environment="staging"
)

stub.GetApplication(application)


# creating audit record entry
application = auditor_pb2.Application(id=2)
session.query(versioning_manager.transaction_cls)


session = Session()
versions = session.query(Animal).first().versions.all()

for version in versions:
	pass

def build_audit_pb(version):
	whodunit = auditor_pb2.Whodunit(
		email=get_email_from_version(version)
	)
	audit = auditor_pb2.Audit(
		application=auditor_pb2.Application(id=2),
		auditable_type=version.version_parent.__class__.__name__,
		auditable_id=version.transaction_id,
		auditable_event_type=version.operation_type,
		auditable_created_at=version.transaction.issued_at.strftime("%Y-%m-%d %H:%M:%S"),
		auditable_whodunit=whodunit,
		auditable_changes=version.changeset,
		auditable_version=version.transaction_id
	)

def get_email_from_version(version):
	transaction_id = version.transaction_id
	transaction = session.execute("select user_info from transaction where id={}".format(version.transaction_id)).first()
	if transaction is None:
		return ''
	else:
		return transaction[0]








class AuditableAudit(object):
	pass


# TODO
# Client to copy data from python service database to auditor service
	# Leave one record in transaction.
	# SELECT * FROM versions JOIN (SELECT item_id, item_type, max(id) as max_version FROM versions GROUP BY item_id, item_type) grouped_versions ON versions.id < grouped_versions.max_version AND versions.item_type = grouped_versions.item_type AND versions.item_id = grouped_versions.item_id LIMIT #{size};
	# your solution should work for multiple models.
	# if there is a way to determine what models are being tracked this becomes easy.

# Reading data from auditor
#
