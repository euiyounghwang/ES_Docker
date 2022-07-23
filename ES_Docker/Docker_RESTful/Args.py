
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interact with Indices with elasticsearch")
    parser.add_argument('--action', dest='action', help='action: create, delete, show, replace, inbox, percolator, put_settings, update', required=True)
    parser.add_argument('--es_host', dest='es_host', help='elasticsearch host name')
    parser.add_argument('--es_index', dest='es_index', help='elasticsearch index name')
    parser.add_argument('--type', dest='type', help='name of the file in mappings')
    parser.add_argument('--settings', dest='settings', help='json string of settings to override')
    parser.add_argument('--shards', dest='shards', help='override the sharding level to use')
    parser.add_argument('--yes', dest='yes', action='store_true', default=False, help='ignore prompts')

    args = parser.parse_args()

    print(args)
    print(args.action, args.es_host)
