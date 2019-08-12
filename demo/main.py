from demo.util import *


def main():
    # 获取数据
    app_desc = get_app_desc()
    apptype_id_name = get_apptype_id_name()
    apptype_train = get_apptype_train()

    # 预判断
    app_desc = get_app_desc_apptype(app_desc, apptype_id_name)

    # 获取label1/label2特征列
    apptype_train = get_label1_label2(apptype_train)

    # 若label2中存在数据则新添加
    apptype_train = add_new_apptype_train_data(apptype_train)

    # 删除出现次数少于5次的数据
    k = DefaultConfig.k
    apptype_train = delete_counts_less_than_k(apptype_train, k)

    # 获取TF-IDF矩阵
    apptype_train, app_desc, apptype_train_term_doc, app_desc_term_doc = get_term_doc(apptype_train, app_desc)

    # 对label1进行labelEncoder
    apptype_train, lbl = get_label_encoder(apptype_train, columns=['label1'])

    if DefaultConfig.select_model is 'lgb':
        # 交叉验证
        stack_train, stack_test = lgb_model(apptype_train, app_desc, apptype_train_term_doc, app_desc_term_doc)
    else:
        # 交叉验证
        stack_train, stack_test = cross_validation(apptype_train, app_desc, apptype_train_term_doc, app_desc_term_doc)

    # 线下准确率+测试结果
    get_offline_accuracy(apptype_train, app_desc, stack_train, stack_test, lbl)


if __name__ == '__main__':
    main()
