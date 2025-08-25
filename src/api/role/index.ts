import request from '@/axios'

export const getRoleListApi = () => {
  return request.get({ url: '/api/role/table' })
}
