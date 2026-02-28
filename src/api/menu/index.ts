import request from '@/axios'

export const getMenuListApi = () => {
  return request.get({ url: '/api/menu/list' })
}
